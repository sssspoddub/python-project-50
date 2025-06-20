from pathlib import Path

from .parsers import parse


def read_file(path: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"No such file: '{path}'")
    return parse(str(p))
