from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Dict, List

from gendiff.nodes import ADDED, NESTED, REMOVED, UNCHANGED, UPDATED

Diff = List[Dict[str, Any]]


def build_diff(data1: Mapping[str, Any], data2: Mapping[str, Any]) -> Diff:
    keys: List[str] = sorted(set(data1) | set(data2))
    diff: Diff = []

    for key in keys:
        if key not in data1:
            diff.append({"key": key, "type": ADDED, "value": data2[key]})
        elif key not in data2:
            diff.append({"key": key, "type": REMOVED, "value": data1[key]})
        elif isinstance(data1[key], Mapping) and isinstance(data2[key], Mapping):
            children = build_diff(data1[key], data2[key])
            diff.append({"key": key, "type": NESTED, "children": children})
        elif data1[key] == data2[key]:
            diff.append({"key": key, "type": UNCHANGED, "value": data1[key]})
        else:
            diff.append(
                {
                    "key": key,
                    "type": UPDATED,
                    "old": data1[key],
                    "new": data2[key],
                },
            )

    return diff
