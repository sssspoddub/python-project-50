from __future__ import annotations

from typing import Any, Dict, List

from gendiff.nodes import ADDED, NESTED, REMOVED, UNCHANGED, UPDATED

INDENT: int = 4
SIGN_SHIFT: int = 2


def _to_str(value: Any, depth: int) -> str:
    if not isinstance(value, dict):
        if isinstance(value, bool):
            return str(value).lower()
        if value is None:
            return "null"
        return str(value)

    indent: str = " " * (depth * INDENT)
    lines: List[str] = [
        f"{indent}{k}: {_to_str(v, depth + 1)}" for k, v in value.items()
    ]
    closing: str = " " * ((depth - 1) * INDENT)
    return "{\n" + "\n".join(lines) + f"\n{closing}}}"


def _format(tree: List[Dict[str, Any]], depth: int) -> str:
    lines: List[str] = []
    base_indent: str = " " * (depth * INDENT - SIGN_SHIFT)

    for node in tree:
        key: str = node["key"]
        kind: str = node["type"]

        if kind == ADDED:
            lines.append(f"{base_indent}+ {key}: {_to_str(node['value'], depth + 1)}")
        elif kind == REMOVED:
            lines.append(f"{base_indent}- {key}: {_to_str(node['value'], depth + 1)}")
        elif kind == UNCHANGED:
            lines.append(f"{base_indent}  {key}: {_to_str(node['value'], depth + 1)}")
        elif kind == UPDATED:
            lines.append(f"{base_indent}- {key}: {_to_str(node['old'], depth + 1)}")
            lines.append(f"{base_indent}+ {key}: {_to_str(node['new'], depth + 1)}")
        elif kind == NESTED:
            children_repr: str = _format(node["children"], depth + 1)
            lines.append(f"{base_indent}  {key}: {children_repr}")

    closing: str = " " * ((depth - 1) * INDENT)
    return "{\n" + "\n".join(lines) + f"\n{closing}}}"


def format_stylish(tree: List[Dict[str, Any]]) -> str:
    return _format(tree, 1)
