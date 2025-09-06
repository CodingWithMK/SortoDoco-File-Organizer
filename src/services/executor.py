from pathlib import Path
import shutil
import os
from domain.models import Plan, Operation

def unique_target(dst: Path) -> Path:
    """
    Rename-with-suffix. If destiation exists, try renaming with 
    "name (1).txt, name (2).txt, ..."
    Stops when a non-existing path found.
    """
    if not dst.exists():
        return dst
    i = 1
    try:
        if dst.exists():
            base_name, _ = os.path.splitext(dst)
            
            dst.rename(f"{dst + i}")
            i += 1
        else:
            dst.rename(f"{dst + i}")
                 
    except Exception as e:
        raise FileExistsError("File {dst} already exists. Try to rename...")
    
        

# TODO: Collision for unique filename