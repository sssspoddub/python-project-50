from collections.abc import Callable
from typing import Dict, List

from .plain import format_plain
from .stylish import format_stylish

_FORMATTERS: Dict[str, Callable[[List[dict]], str]] = {
    "plain": format_plain,
    "stylish": format_stylish,
}


def choose(name: str) -> Callable[[List[dict]], str]:
    try:
        return _FORMATTERS[name]
    except KeyError as exc:
        raise ValueError(f"Unknown format: {name}") from exc
