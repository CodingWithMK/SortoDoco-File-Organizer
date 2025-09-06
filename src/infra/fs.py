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
    source = os.path.join(downloads_dir)
    
    if source:
        for category in categories:
            os.path.join(category)
            if not os.path.exists(session_ts):
                os.makedirs(session_ts, exist_ok=True, parents=True)
    
        return session_ts