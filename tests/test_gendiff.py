import pytest
from gendiff.gendiff import generate_diff
from pathlib import Path

def test_generate_diff_stylish(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    file1.write_text('{"key": "value1"}')
    file2.write_text('{"key": "value2"}')

    result = generate_diff(str(file1), str(file2), 'stylish')
    assert 'changed' in result or 'value2' in result

def test_generate_diff_plain(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    file1.write_text('{"key": "value1"}')
    file2.write_text('{"key": "value2"}')

    result = generate_diff(str(file1), str(file2), 'plain')
    assert 'was updated' in result

def test_generate_diff_unknown_format(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    file1.write_text('{"key": "value1"}')
    file2.write_text('{"key": "value2"}')

    with pytest.raises(ValueError):
        generate_diff(str(file1), str(file2), 'unknown')
