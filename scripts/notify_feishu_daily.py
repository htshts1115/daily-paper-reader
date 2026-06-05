#!/usr/bin/env python3
"""Send the latest Daily Paper Reader recommendation summary to a Feishu group."""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_SITE_URL = "https://htshts1115.github.io/daily-paper-reader/"
DEFAULT_BRIEF = "今日推荐已更新，请查看完整日报。"
MAX_PAYLOAD_CHARS = 15_000


def find_latest_recommend_json(root: Path) -> Path:
    """Return the recommendation JSON with the latest valid ``generated_at``."""
    candidates = sorted(root.glob("archive/*/recommend/arxiv_papers_*.standard.json"))
    if not candidates:
        raise FileNotFoundError(
            "No recommendation JSON found: archive/*/recommend/"
            "arxiv_papers_*.standard.json"
        )

    generated_candidates: list[tuple[datetime, Path]] = []
    for path in candidates:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            generated_at = data.get("generated_at")
            if not isinstance(generated_at, str) or not generated_at:
                continue
            generated_time = datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
            if generated_time.tzinfo is None:
                generated_time = generated_time.replace(tzinfo=timezone.utc)
            generated_candidates.append((generated_time.astimezone(timezone.utc), path))
        except (OSError, json.JSONDecodeError, ValueError, AttributeError):
            # Keep unreadable or malformed files in the path-sorted fallback set.
            continue

    if generated_candidates:
        return max(generated_candidates, key=lambda item: (item[0], str(item[1])))[1]
    return candidates[-1]


def extract_daily_brief(readme_path: Path) -> str:
    """Extract the AI daily brief section from docs/README.md."""
    try:
        lines = readme_path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return DEFAULT_BRIEF

    heading = "### 今日简报（AI）"
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == heading) + 1
    except StopIteration:
        return DEFAULT_BRIEF

    section: list[str] = []
    for line in lines[start:]:
        if line.lstrip().startswith("#"):
            break
        if line.strip().startswith("- 详情："):
            continue
        section.append(line.rstrip())

    brief = "\n".join(section).strip()
    return brief or DEFAULT_BRIEF


def normalize_paper(paper: dict[str, Any]) -> dict[str, Any]:
    """Select the fields needed by the notification and normalize its tag."""
    tags = paper.get("llm_tags") or []
    first_tag = tags[0] if isinstance(tags, list) and tags else ""
    tag = paper.get("matched_query_tag") or first_tag or ""
    if isinstance(tag, str) and tag.startswith("query:"):
        tag = tag.removeprefix("query:")

    return {
        "title": paper.get("title", ""),
        "score": paper.get("llm_score"),
        "tag": tag,
        "evidence": paper.get("llm_evidence_cn")
        or paper.get("llm_evidence")
        or "",
        "tldr": paper.get("llm_tldr_cn") or paper.get("llm_tldr") or "",
        "link": paper.get("link", ""),
    }


def select_top_papers(papers: list[dict[str, Any]], top_k: int) -> list[dict[str, Any]]:
    """Sort deep-dive papers by LLM score and return normalized Top K entries."""
    def score_value(paper: dict[str, Any]) -> float:
        try:
            return float(paper.get("llm_score"))
        except (TypeError, ValueError):
            return float("-inf")

    selected = sorted(papers, key=score_value, reverse=True)[: max(top_k, 0)]
    return [normalize_paper(paper) for paper in selected]


def make_feishu_sign(timestamp: str, secret: str) -> str:
    """Create a Feishu custom bot signature."""
    string_to_sign = f"{timestamp}\n{secret}"
    digest = hmac.new(
        string_to_sign.encode("utf-8"),
        b"",
        digestmod=hashlib.sha256,
    ).digest()
    return base64.b64encode(digest).decode("utf-8")


def _format_score(score: Any) -> str:
    if score is None or score == "":
        return "-"
    try:
        return f"{float(score):.1f}"
    except (TypeError, ValueError):
        return str(score)


def _paper_block(index: int, paper: dict[str, Any], compact: bool) -> list[dict[str, str]]:
    title = str(paper.get("title") or "（无标题）")
    score = _format_score(paper.get("score"))
    tag = str(paper.get("tag") or "-")
    link = str(paper.get("link") or "")
    evidence = str(paper.get("evidence") or "")
    if compact:
        title = title[:300]
        tag = tag[:100]
        link = link[:1000]

    elements: list[dict[str, str]] = [
        {"tag": "text", "text": f"{index}. {title}\n评分：{score}/10\n方向：{tag}\n"}
    ]
    if not compact and evidence:
        elements.append({"tag": "text", "text": f"理由：{evidence}\n"})
    if link:
        elements.extend(
            [
                {"tag": "text", "text": "PDF："},
                {"tag": "a", "text": link, "href": link},
                {"tag": "text", "text": "\n\n"},
            ]
        )
    else:
        elements.append({"tag": "text", "text": "PDF：-\n\n"})
    return elements


def build_post_payload(
    *,
    date: str,
    stats: dict[str, Any],
    brief: str,
    papers: list[dict[str, Any]],
    site_url: str,
    compact: bool = False,
) -> dict[str, Any]:
    """Build a Feishu post rich-text payload."""
    deep_count = stats.get("deep_selected", len(papers))
    quick_count = stats.get("quick_selected", 0)
    total_count = stats.get("total")
    if total_count is None:
        try:
            total_count = int(deep_count) + int(quick_count)
        except (TypeError, ValueError):
            total_count = "-"

    content: list[list[dict[str, str]]] = [
        [
            {
                "tag": "text",
                "text": (
                    f"本次总论文数：{total_count}\n"
                    f"精读区：{deep_count}\n"
                    f"速读区：{quick_count}\n"
                ),
            }
        ],
        [{"tag": "text", "text": f"今日简报：\n{brief}\n"}],
        [{"tag": "text", "text": "Top 精读论文：\n"}],
    ]
    for index, paper in enumerate(papers, start=1):
        content.append(_paper_block(index, paper, compact))
    content.append(
        [
            {"tag": "text", "text": "完整日报："},
            {"tag": "a", "text": "点击查看", "href": site_url},
        ]
    )

    return {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": f"虚化组论文推荐日报｜{date}",
                    "content": content,
                }
            }
        },
    }


def _payload_chars(payload: dict[str, Any]) -> int:
    return len(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))


def build_limited_payload(
    *,
    date: str,
    stats: dict[str, Any],
    brief: str,
    papers: list[dict[str, Any]],
    site_url: str,
) -> dict[str, Any]:
    """Build a payload and progressively reduce it to stay below the hard limit."""
    payload = build_post_payload(
        date=date, stats=stats, brief=brief, papers=papers, site_url=site_url
    )
    if _payload_chars(payload) <= MAX_PAYLOAD_CHARS:
        return payload

    payload = build_post_payload(
        date=date, stats=stats, brief=brief, papers=papers[:3], site_url=site_url
    )
    if _payload_chars(payload) <= MAX_PAYLOAD_CHARS:
        return payload

    payload = build_post_payload(
        date=date,
        stats=stats,
        brief=brief,
        papers=papers[:3],
        site_url=site_url,
        compact=True,
    )
    if _payload_chars(payload) <= MAX_PAYLOAD_CHARS:
        return payload

    # A generated brief can unexpectedly be very long; retain a useful prefix.
    return build_post_payload(
        date=date,
        stats=stats,
        brief=brief[:2000] + "…",
        papers=papers[:3],
        site_url=site_url,
        compact=True,
    )


def attach_signature(payload: dict[str, Any], secret: str) -> dict[str, Any]:
    """Return a copy of the payload with signature fields when configured."""
    if not secret:
        return payload
    timestamp = str(int(time.time()))
    return {"timestamp": timestamp, "sign": make_feishu_sign(timestamp, secret), **payload}


def send_notification(webhook: str, payload: dict[str, Any]) -> bool:
    """Send the payload. Return False when no webhook is configured."""
    if not webhook:
        print("FEISHU_BOT_WEBHOOK is empty, skip notification.")
        return False

    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        webhook,
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            response_body = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        response_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Feishu webhook HTTP error {exc.code}: {response_body}"
        ) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Feishu webhook request failed: {exc.reason}") from exc

    try:
        result = json.loads(response_body)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Feishu webhook returned invalid JSON: {response_body}") from exc

    code = result.get("code", result.get("StatusCode"))
    message = result.get("msg", result.get("StatusMessage", ""))
    if code != 0:
        raise RuntimeError(f"Feishu webhook returned error code {code}: {message}")

    print("Feishu notification sent successfully.")
    return True


def _generated_date(generated_at: Any) -> str:
    if isinstance(generated_at, str) and generated_at:
        try:
            return datetime.fromisoformat(generated_at.replace("Z", "+00:00")).date().isoformat()
        except ValueError:
            return generated_at[:10]
    return datetime.now().date().isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the payload without sending a webhook request",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent directory of scripts/)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    webhook = os.environ.get("FEISHU_BOT_WEBHOOK", "").strip()
    if not webhook and not args.dry_run:
        send_notification(webhook, {})
        return 0

    recommend_path = find_latest_recommend_json(args.root)
    print(f"Using recommendation JSON: {recommend_path.relative_to(args.root)}")
    data = json.loads(recommend_path.read_text(encoding="utf-8"))

    try:
        top_k = max(int(os.environ.get("FEISHU_NOTIFY_TOP_K", "5")), 0)
    except ValueError as exc:
        raise ValueError("FEISHU_NOTIFY_TOP_K must be an integer") from exc

    papers = select_top_papers(data.get("deep_dive") or [], top_k)
    payload = build_limited_payload(
        date=_generated_date(data.get("generated_at")),
        stats=data.get("stats") or {},
        brief=extract_daily_brief(args.root / "docs" / "README.md"),
        papers=papers,
        site_url=os.environ.get("DAILY_PAPER_SITE_URL", DEFAULT_SITE_URL).strip()
        or DEFAULT_SITE_URL,
    )
    payload = attach_signature(payload, os.environ.get("FEISHU_BOT_SECRET", "").strip())

    if args.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    send_notification(webhook, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
