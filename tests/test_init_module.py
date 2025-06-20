import json
import pytest
from pathlib import Path

from gendiff import generate_diff
from gendiff.readers import read_file
from gendiff.parsers import parse


SIMPLE_JSON = '{"a": 1, "b": true}'


def test_parse_mapping():
    mapping = {"x": 10, "y": False}
    assert parse(mapping) == {"x": 10, "y": False}


def test_parse_json(tmp_path: Path):
    f = tmp_path / "file.json"
    f.write_text(SIMPLE_JSON)
    data = parse(str(f))
    assert data == {"a": 1, "b": "true"}  # у нас lowercase-строки


def test_parse_yaml(tmp_path: Path):
    yaml = tmp_path / "file.yml"
    yaml.write_text("foo: bar\nnested:\n  x: 5")
    data = parse(str(yaml))
    assert data == {"foo": "bar", "nested": {"x": 5}}


def test_parse_unsupported_ext():
    with pytest.raises(ValueError) as exc:
        parse("no_such.ext")
    assert "Unsupported file type" in str(exc.value)


def test_read_file_json(tmp_path: Path):
    f = tmp_path / "file.json"
    f.write_text(SIMPLE_JSON)
    assert read_file(str(f)) == {"a": 1, "b": "true"}


def test_read_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_file("does_not_exist.json")


def test_generate_diff_minimal(tmp_path: Path):
    f1 = tmp_path / "a.json"
    f2 = tmp_path / "b.json"
    f1.write_text('{"k": 1}')
    f2.write_text('{"k": 2}')
    out = generate_diff(str(f1), str(f2), format_name="stylish")
    assert "- k: 1" in out
    assert "+ k: 2" in out
