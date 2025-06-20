from gendiff.nodes import ADDED, REMOVED
from gendiff.tree import build_diff


def test_build_diff_add_and_remove():
    first = {"a": 1}
    second = {"b": 2}
    diff = build_diff(first, second)

    types = set(node["type"] for node in diff)
    assert types == {ADDED, REMOVED}

    assert any(node["key"] == "b" and node["type"] == ADDED for node in diff)
    assert any(node["key"] == "a" and node["type"] == REMOVED for node in diff)
