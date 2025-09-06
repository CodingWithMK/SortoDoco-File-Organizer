from pathlib import Path

def unique_target(dst: Path) -> Path:
    """
    If `dst` exists, return a new Path like
    'name (1).ext', 'name (2).ext', ... that doesn't exist yet.
    Otherwise return `dst` unchanged.
    """

    if not dst.exists():
        return dst
    
    parent = dst.parent
    stem = dst.stem
    suffix = dst.suffix

    i = 1
    while True:
        candidate = parent / f"{stem} ({i}){suffix}"

        if not candidate.exists():
            return candidate
        
        i += 1

target = Path("essay.txt")
new_target = unique_target(target)
print(new_target)