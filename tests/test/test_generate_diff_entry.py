import json

import pytest

from gendiff import generate_diff

D1 = {"foo": 1, "bar": {"x": True}}
D2 = {"foo": 2, "bar": {"x": False}, "baz": "new"}


def test_generate_diff_default_stylish(tmp_path):
    f1 = tmp_path / "one.json"
    f2 = tmp_path / "two.json"
    f1.write_text(json.dumps(D1))
    f2.write_text(json.dumps(D2))

    out = generate_diff(str(f1), str(f2))
    assert "- foo: 1" in out
    assert "+ foo: 2" in out
    assert "+ baz: new" in out
    assert "- bar: {" not in out


def test_generate_diff_plain_and_json(tmp_path):
    f1 = tmp_path / "one.json"
    f2 = tmp_path / "two.json"
    f1.write_text(json.dumps(D1))
    f2.write_text(json.dumps(D2))

    plain = generate_diff(str(f1), str(f2), format_name="plain")
    assert "Property 'foo' was updated. From 1 to 2" in plain
    assert "Property 'baz' was added with value: 'new'" in plain
    assert "Property 'bar.x' was updated. From true to false" in plain

    js = generate_diff(str(f1), str(f2), format_name="json")
    tree = json.loads(js)
    assert isinstance(tree, list)
    keys = [node["key"] for node in tree]
    for expected in ("foo", "bar", "baz"):
        assert expected in keys


def test_generate_diff_invalid_path():
    with pytest.raises(FileNotFoundError):
        generate_diff("no_such_file.yml", "also_nope.json")


def test_generate_diff_unsupported_format(tmp_path):
    f = tmp_path / "one.json"
    f.write_text(json.dumps(D1))
    with pytest.raises(ValueError):
        generate_diff(str(f), str(f), format_name="xml")
