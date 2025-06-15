from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

import yaml

_JSON_EXT = {".json"}
_YAML_EXT = {".yml", ".yaml"}


def _lowercase_bools(obj: Any) -> Any:
    if isinstance(obj, bool):
        return str(obj).lower()
    if isinstance(obj, list):
        return [_lowercase_bools(x) for x in obj]
    if isinstance(obj, Mapping):
        return {k: _lowercase_bools(v) for k, v in obj.items()}
    return obj


def parse(path: str | Path | Mapping) -> dict:
    if isinstance(path, Mapping):
        return dict(path)

    p = Path(path)
    ext = p.suffix.lower()

    if ext in _JSON_EXT:
        data = json.load(p.open())
        return _lowercase_bools(data)

    if ext in _YAML_EXT:
        return yaml.safe_load(p.open())

    raise ValueError(f"Unsupported file type: {ext}")
