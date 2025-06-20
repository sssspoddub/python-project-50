from pathlib import Path

import pytest

from gendiff.parsers import parse
from gendiff.readers import read_file

SIMPLE_JSON = """
{
  "a": 1,
  "b": true
}
"""


def test_parse_mapping():
    data = {"x": 10, "y": False}
    result = parse(data)
    assert result == {"x": 10, "y": False}


def test_parse_json(tmp_path: Path):
    f = tmp_path / "data.json"
    f.write_text(SIMPLE_JSON)
    parsed = parse(str(f))
    assert parsed == {"a": 1, "b": "true"}


def test_parse_yaml(tmp_path: Path):
    yaml_content = """
x: 5
y: false
"""
    f = tmp_path / "data.yml"
    f.write_text(yaml_content)
    parsed = parse(str(f))
    assert parsed == {"x": 5, "y": False}


def test_read_file_json(tmp_path: Path):
    f = tmp_path / "data.json"
    f.write_text(SIMPLE_JSON)
    data = read_file(str(f))
    assert data == {"a": 1, "b": "true"}


def test_read_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_file("no_such.file")
