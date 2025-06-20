import json

from gendiff.formatters.json import format_json

def test_format_json_empty_list():
    tree = []
    expected = json.dumps(tree, indent=4, sort_keys=True)
    assert format_json(tree) == expected

def test_format_json_single_object_sorted_keys_and_indent():
    tree = [{"b": 2, "a": 1}]
    expected = json.dumps(tree, indent=4, sort_keys=True)
    assert format_json(tree) == expected

def test_format_json_nested_structures():
    tree = [
        {"z": [3, 2, 1], "y": {"b": True, "a": None}}
    ]
    expected = json.dumps(tree, indent=4, sort_keys=True)
    assert format_json(tree) == expected
