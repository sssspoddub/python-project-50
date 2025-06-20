from typing import Any, Dict, List

from gendiff.nodes import ADDED, NESTED, REMOVED, UPDATED

_INDENT = 4


def _stringify(value: Any) -> str:

    if isinstance(value, dict):
        return "[complex value]"

    if value is True or value == "true":
        return "true"
    if value is False or value == "false":
        return "false"
    if value is None or value == "null":
        return "null"

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)


def _walk(nodes: List[Dict[str, Any]], ancestry: List[str] | None = None) -> List[str]:
    if ancestry is None:
        ancestry = []
    lines: List[str] = []

    for node in nodes:
        key = node["key"]
        kind = node["type"]
        prop_path = ".".join(ancestry + [key])

        if kind == ADDED:
            value_repr = _stringify(node["value"])
            lines.append(f"Property '{prop_path}' was added with value: {value_repr}")
        elif kind == REMOVED:
            lines.append(f"Property '{prop_path}' was removed")
        elif kind == UPDATED:
            old_repr = _stringify(node["old"])
            new_repr = _stringify(node["new"])
            lines.append(
                f"Property '{prop_path}' was updated. From {old_repr} to {new_repr}"
            )
        elif kind == NESTED:
            lines.extend(_walk(node["children"], ancestry + [key]))

    return lines


def format_plain(tree: List[Dict[str, Any]]) -> str:
    return "\n".join(_walk(tree))
