import importlib.util
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import Mock, patch

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("direct_arxiv_fetcher", ROOT / "src/maintain/fetchers/fetch_arxiv.py")
fetcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fetcher)


def test_categories_are_configurable_and_deduplicated():
    with patch.dict("os.environ", {"DPR_ARXIV_CATEGORIES": "cs.CV,cs.LG,cs.CV"}):
        assert fetcher.resolve_fetch_categories() == ["cs.CV", "cs.LG"]
    with patch.dict("os.environ", {"DPR_ARXIV_CATEGORIES": ""}):
        assert fetcher.resolve_fetch_categories() == fetcher.CATEGORIES_TO_FETCH


def test_failed_fetch_raises_instead_of_becoming_empty_success():
    client = Mock()
    client.results.side_effect = RuntimeError("network unavailable")
    end = datetime(2026, 11, 6, tzinfo=timezone.utc)
    with patch.dict("os.environ", {"DPR_ARXIV_DIRECT_FETCH": "1"}):
        with pytest.raises(RuntimeError, match="不更新抓取水位"):
            fetcher.fetch_category_in_windows(client, "cs.CV", [(end - timedelta(days=1), end)], set(), {})


def test_recovery_workflow_keeps_cloud_models_and_cost_controls():
    workflow = yaml.safe_load((ROOT / ".github/workflows/daily-paper-reader.yml").read_text())
    env = workflow["jobs"]["run"]["env"]
    assert env["DPR_ARXIV_DIRECT_FETCH"] == "1"
    assert env["DPR_ARXIV_CATEGORIES"] == "cs.CV,cs.LG,cs.AI,eess.IV"
    assert env["DPR_MODELS_REMOTE_ONLY"] == "1"
    assert env["DPR_RERANK_GLOBAL_POOL_LIMIT"] == "120"
