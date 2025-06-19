from pathlib import Path
from typing import Mapping

from gendiff.parsers import parse


def read_file(path: str | Path | Mapping) -> dict:
    return parse(path)
