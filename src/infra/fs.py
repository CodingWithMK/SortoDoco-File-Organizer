from pathlib import Path
from typing import Iterable
from datetime import datetime
import os

def ensure_session_dirs(downloads_dir: Path,
                        categories: Iterable[str],
                        session_ts: str) -> dict[str, Path]:
    """
    Returns mapping {category: session_dir} and ensures they exist.
    Also ensures _Misc/session_ts exists.
    """
    for category in categories:
        session_dirs = os.path.join(downloads_dir, category, datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        
        if not os.path.exists(session_dirs):
            os.makedirs(session_dirs, exist_ok=True, parents=True)
    
    return session_dirs