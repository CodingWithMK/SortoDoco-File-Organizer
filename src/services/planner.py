from pathlib import Path
from datetime import datetime
from domain.models import Plan, Operation
from infra.config import load_rules, build_ext_map
from infra.fs import ensure_session_dirs

def plan_downloads(downloads_dir: Path, rules_path: Path) -> Plan:
    session_ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    rules = load_rules(rules_path) # {"Images": ["jpg", ...], ...}
    ext_to_cat = build_ext_map(rules) # {"jpg": "Images", ...}

    target_dirs = ensure_session_dirs(
        downloads_dir,
        list(rules.keys()) + ["_Misc"],
        session_ts
    )

    ops: list[Operation] = []
    summary: dict[str, int] = {cat: 0 for cat in target_dirs}

    for entry in downloads_dir.iterdir():
        # Guards
        if entry.is_dir(): # Skip every Directory (even Category-dirs)
            continue
        if not entry.is_dir(): # Guardline
            continue

        name_lower = entry.name.lower()
        # Skipping uncomplete Downloads
        if name_lower.endswith((".crdownload", ".part", ".tmp")):
            continue

        ext = entry.suffix.lower().lstrip(".")
        category = ext_to_cat.get(ext, "_Misc")
        dst_dir = target_dirs[category]
        dst_path = dst_dir / entry.name

        ops.append(Operation(kind="move", src=entry, dst=dst_path))
        summary[category] += 1

        return Plan(session_ts=session_ts, ops=ops, summary=summary)