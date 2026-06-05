import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "notify_feishu_daily", ROOT / "scripts" / "notify_feishu_daily.py"
)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MOD)


class NotifyFeishuDailyTest(unittest.TestCase):
    def test_select_top_papers_normalizes_and_sorts_by_score(self):
        papers = [
            {"title": "Low", "llm_score": 8, "llm_tags": ["query:seg"]},
            {
                "title": "High",
                "llm_score": 10,
                "matched_query_tag": "query:mono-depth",
                "llm_evidence_cn": "推荐理由",
            },
            {"title": "Middle", "llm_score": 9},
        ]

        selected = MOD.select_top_papers(papers, 2)

        self.assertEqual([paper["title"] for paper in selected], ["High", "Middle"])
        self.assertEqual(selected[0]["tag"], "mono-depth")
        self.assertEqual(selected[0]["evidence"], "推荐理由")

    def test_extract_daily_brief_stops_at_next_heading_and_skips_detail_link(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            readme = Path(tmpdir) / "README.md"
            readme.write_text(
                "# 日报\n\n### 今日简报（AI）\n第一行。\n- 详情：[日报](/daily)\n\n### 精读区\n内容\n",
                encoding="utf-8",
            )

            brief = MOD.extract_daily_brief(readme)

        self.assertEqual(brief, "第一行。")

    def test_make_feishu_sign_is_non_empty(self):
        sign = MOD.make_feishu_sign("1710000000", "secret")

        self.assertTrue(sign)
        self.assertIsInstance(sign, str)

    def test_empty_webhook_skips_send(self):
        self.assertFalse(MOD.send_notification("", {"msg_type": "post"}))

    def test_large_payload_drops_evidence_and_stays_below_limit(self):
        papers = [
            {
                "title": f"Paper {index}",
                "score": 10,
                "tag": "mono-depth",
                "evidence": "很长的推荐理由" * 3000,
                "link": "https://example.com/paper.pdf",
            }
            for index in range(5)
        ]

        payload = MOD.build_limited_payload(
            date="2026-06-04",
            stats={"deep_selected": 5, "quick_selected": 2},
            brief="今日简报",
            papers=papers,
            site_url="https://example.com/",
        )

        self.assertLessEqual(MOD._payload_chars(payload), MOD.MAX_PAYLOAD_CHARS)
        serialized = json.dumps(payload, ensure_ascii=False)
        self.assertNotIn("很长的推荐理由", serialized)


    def test_load_daily_report_prefers_current_docs_over_archive_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            docs = root / "docs"
            report_dir = docs / "202606" / "04"
            report_dir.mkdir(parents=True)
            archive_recommend = (
                root
                / "archive"
                / "old"
                / "recommend"
                / "arxiv_papers_old.standard.json"
            )
            archive_recommend.parent.mkdir(parents=True)
            archive_recommend.write_text(
                json.dumps(
                    {
                        "generated_at": "2026-06-05T00:00:00+00:00",
                        "stats": {"deep_selected": 15, "quick_selected": 19},
                        "deep_dive": [
                            {
                                "title": "Archive Paper",
                                "llm_score": 10,
                                "matched_query_tag": "query:archive",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (docs / "README.md").write_text(
                "\n".join(
                    [
                        "## 每次日报",
                        "- 本次总论文数：34",
                        "- 详情：[/202606/04/README](/202606/04/README)",
                    ]
                ),
                encoding="utf-8",
            )
            (report_dir / "README.md").write_text(
                "\n".join(
                    [
                        "# 日报 · 2026-06-04",
                        "",
                        "- 生成时间：2026-06-04 00:00:00 UTC",
                        "- 当次推荐总数：15",
                        "- 精读区：4",
                        "- 速读区：11",
                        "",
                        "## 今日简报（AI）",
                        "详情页简报。",
                        "",
                        "## 精读区",
                        "1. [Doc Paper One](/202606/04/paper-one) （9.5/10）",
                        "2. [Doc Paper Two](/202606/04/paper-two) （8.0/10）",
                        "",
                        "## 速读区",
                    ]
                ),
                encoding="utf-8",
            )
            (report_dir / "paper-one.md").write_text(
                "\n".join(
                    [
                        "---",
                        'title: "Doc Paper One FM"',
                        'pdf: "https://example.com/one.pdf"',
                        'tags: ["query:mono-depth"]',
                        "score: 9.5",
                        "evidence: 来自论文详情一",
                        "tldr: 摘要一",
                        "---",
                    ]
                ),
                encoding="utf-8",
            )
            (report_dir / "paper-two.md").write_text(
                "\n".join(
                    [
                        "---",
                        'title: "Doc Paper Two FM"',
                        'pdf: "https://example.com/two.pdf"',
                        'tags: ["query:seg"]',
                        "score: 8.0",
                        "evidence: 来自论文详情二",
                        "---",
                    ]
                ),
                encoding="utf-8",
            )

            report = MOD.load_daily_report(root, 2)

        self.assertEqual(report["source"], "docs/202606/04/README.md")
        self.assertEqual(report["date"], "2026-06-04")
        self.assertEqual(report["stats"], {"total": 15, "deep_selected": 4, "quick_selected": 11})
        self.assertEqual(report["brief"], "详情页简报。")
        self.assertEqual([paper["title"] for paper in report["papers"]], ["Doc Paper One FM", "Doc Paper Two FM"])
        self.assertEqual([paper["score"] for paper in report["papers"]], ["9.5", "8.0"])
        self.assertEqual([paper["tag"] for paper in report["papers"]], ["mono-depth", "seg"])
        self.assertEqual(report["papers"][0]["evidence"], "来自论文详情一")
        self.assertEqual(report["papers"][0]["link"], "https://example.com/one.pdf")

    def test_find_latest_recommend_json_prefers_generated_at_over_mtime(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            old = root / "archive" / "20260101" / "recommend" / "arxiv_papers_old.standard.json"
            new = root / "archive" / "20260102" / "recommend" / "arxiv_papers_new.standard.json"
            old.parent.mkdir(parents=True)
            new.parent.mkdir(parents=True)
            old.write_text(
                json.dumps({"generated_at": "2026-01-01T12:00:00+00:00"}),
                encoding="utf-8",
            )
            new.write_text(
                json.dumps({"generated_at": "2026-01-02T12:00:00+00:00"}),
                encoding="utf-8",
            )
            old_mtime = new.stat().st_mtime + 60
            os.utime(old, (old_mtime, old_mtime))

            latest = MOD.find_latest_recommend_json(root)

        self.assertEqual(latest.name, new.name)

    def test_find_latest_recommend_json_falls_back_to_last_path(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            first = root / "archive" / "20260101" / "recommend" / "arxiv_papers_first.standard.json"
            last = root / "archive" / "20260102" / "recommend" / "arxiv_papers_last.standard.json"
            first.parent.mkdir(parents=True)
            last.parent.mkdir(parents=True)
            first.write_text("not json", encoding="utf-8")
            last.write_text(json.dumps({"generated_at": "invalid"}), encoding="utf-8")

            latest = MOD.find_latest_recommend_json(root)

        self.assertEqual(latest.name, last.name)


if __name__ == "__main__":
    unittest.main()
