"""Diff generator for flat JSON files."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from .readers import read_file


def _stringify(value: Any) -> str:
    """Convert Python value to CLI-friendly representation."""
    if isinstance(value, bool):            # true/false в нижнем регистре
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def _build_ast(data1: Mapping[str, Any], data2: Mapping[str, Any]) -> list[str]:
    """Return list of diff lines with proper prefixes."""
    lines: list[str] = []
    for key in sorted(set(data1) | set(data2)):
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                lines.append(f"    {key}: {_stringify(data1[key])}")
            else:
                lines.append(f"  - {key}: {_stringify(data1[key])}")
                lines.append(f"  + {key}: {_stringify(data2[key])}")
        elif key in data1:
            lines.append(f"  - {key}: {_stringify(data1[key])}")
        else:  # key only in data2
            lines.append(f"  + {key}: {_stringify(data2[key])}")
    return lines


def generate_diff(path1: str | Path, path2: str | Path) -> str:
    """Generate diff string between two flat-JSON files."""
    data1 = read_file(path1)
    data2 = read_file(path2)
    body = "\n".join(_build_ast(data1, data2))
    return "{\n" + body + "\n}"
