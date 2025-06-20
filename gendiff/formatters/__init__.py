from __future__ import annotations

from collections.abc import Callable
from typing import Dict, List

from .json import format_json
from .plain import format_plain
from .stylish import format_stylish

_FORMATTERS: Dict[str, Callable[[List[dict]], str]] = {
    "plain": format_plain,
    "stylish": format_stylish,
    "json": format_json,
}


def choose(name: str) -> Callable[[List[dict]], str]:
    try:
        return _FORMATTERS[name]
    except KeyError as exc:
        raise ValueError(f"Unknown format: {name}") from exc


__all__ = ["choose"]
