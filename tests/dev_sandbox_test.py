from pathlib import Path
import sys, shutil

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT  = REPO_ROOT / "src"
sys.path.insert(0, str(SRC_ROOT))

from domain.models import Plan
from services.planner import plan_downloads
from services.executor import apply_plan

def setup_dummy_files(root: Path):
    # Create Dummy Data
    for name in ["pic.JPG", "readme.PDF", "clip.mp4", "data.csv", "weridfile", "readme.pdf"]:
        (root / name).write_bytes(b"dummy")


def print_plan(plan: Plan):
    print(f"Session: {plan.session_ts}")
    print("Summary:", plan.summary)
    print("First ops:")
    for op in plan.ops[:5]:
        print("  ", op.src.name, "->", op.dst)


if __name__ == "__main__":
    sandbox    = REPO_ROOT / "SANDBOX_DOWNLOADS"
    rules_path = SRC_ROOT / "rules" / "extensions.json"
    
    # 1) Clean & Setup
    if sandbox.exists():
        # Caution: Deletes the Sandbox-information
        shutil.rmtree(sandbox)
    sandbox.mkdir(parents=True, exist_ok=True)
    setup_dummy_files(sandbox)

    # 2) Plan
    plan = plan_downloads(sandbox, rules_path)
    print_plan(plan)

    # 3) Apply
    report = apply_plan(plan)
    print("Report:", report)