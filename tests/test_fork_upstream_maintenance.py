import unittest
from pathlib import Path


WORKFLOW = Path(".github/workflows/fork-upstream-maintenance.yml")
ATTRIBUTES = Path(".gitattributes")


class ForkUpstreamMaintenanceContractTest(unittest.TestCase):
    def test_sync_runs_daily_and_remains_manually_triggerable(self):
        text = WORKFLOW.read_text(encoding="utf-8")

        self.assertIn("workflow_dispatch:", text)
        self.assertIn("push:", text)
        self.assertIn('".github/workflows/fork-upstream-maintenance.yml"', text)
        self.assertIn("schedule:", text)
        self.assertIn('cron: "0 17 * * *"', text)
        self.assertIn("ref: main", text)
        self.assertIn("group: upstream-sync", text)

    def test_sync_uses_safe_merge_without_force_push(self):
        text = WORKFLOW.read_text(encoding="utf-8")

        self.assertIn("git config merge.ours.driver true", text)
        self.assertIn("git fetch --prune upstream main", text)
        self.assertIn('git merge --no-edit -m "[sync] merge upstream/main" upstream/main', text)
        self.assertIn("git push origin HEAD:main", text)
        self.assertIn("git merge --abort", text)
        self.assertNotIn("--force", text)

    def test_runtime_conflicts_are_automatic_but_code_conflicts_stop(self):
        text = WORKFLOW.read_text(encoding="utf-8")

        for pattern in (
            "archive/*",
            "docs/[0-9]*/*",
            "docs/conference/*",
            "docs/assets/figures/*",
            "docs/assets/tables/*",
        ):
            self.assertIn(pattern, text)
        self.assertIn("unresolved+=(\"$path\")", text)
        self.assertIn("$GITHUB_STEP_SUMMARY", text)

    def test_generated_data_has_merge_ours_protection(self):
        text = ATTRIBUTES.read_text(encoding="utf-8")

        for rule in (
            "archive/** merge=ours",
            "docs/[0-9]*/** merge=ours",
            "docs/conference/** merge=ours",
            "docs/assets/figures/** merge=ours",
            "docs/assets/tables/** merge=ours",
        ):
            self.assertIn(rule, text)


if __name__ == "__main__":
    unittest.main()
