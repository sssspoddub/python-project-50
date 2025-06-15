from pathlib import Path
from typing import Mapping

from gendiff.readers import read_file


def _ensure_mapping(src: str | Path | Mapping) -> dict:
    if isinstance(src, Mapping):
        return dict(src)
    return read_file(src)


def _stringify(val) -> str:
    return str(val)


def generate_diff(
    file1: str | Path | Mapping,
    file2: str | Path | Mapping,
    *,
    fmt: str = "stylish",
) -> str:
    if fmt != "stylish":
        raise ValueError(f"unknown format: {fmt}")

    d1, d2 = map(_ensure_mapping, (file1, file2))

    lines: list[str] = ["{"]

    for key in sorted(d1.keys() | d2.keys()):
        in1, in2 = key in d1, key in d2

        if in1 and not in2:  # removed
            lines.append(f"  - {key}: {_stringify(d1[key])}")
        elif not in1 and in2:  # added
            lines.append(f"  + {key}: {_stringify(d2[key])}")
        elif d1[key] == d2[key]:  # unchanged
            lines.append(f"    {key}: {_stringify(d1[key])}")
        else:  # changed
            lines.append(f"  - {key}: {_stringify(d1[key])}")
            lines.append(f"  + {key}: {_stringify(d2[key])}")

    lines.append("}")
    return "\n".join(lines)
