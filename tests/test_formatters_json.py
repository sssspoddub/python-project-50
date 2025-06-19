import json
import pytest

from gendiff.formatters.json import format_json


@pytest.fixture
def sample_tree():
    return [
        {"key": "a", "type": "UNCHANGED", "value": 1},
        {"key": "b", "type": "UPDATED", "old_value": True, "new_value": False},
        {"key": "c", "type": "REMOVED", "value": None},
    ]


def test_format_json_returns_valid_json(sample_tree):
    s = format_json(sample_tree)
    # Проверяем, что это строка, которую можно распарсить обратно
    parsed = json.loads(s)
    assert isinstance(parsed, list)
    # Содержит те же словари
    assert parsed == sample_tree


def test_format_json_indentation_and_sort_keys(sample_tree, tmp_path):
    # Запишем в файл, чтобы проверить форматирование
    out_file = tmp_path / "out.json"
    out_file.write_text(format_json(sample_tree))
    text = out_file.read_text().splitlines()
    # Первая строка должна быть '['
    assert text[0].strip() == "["
    # Последняя строка должна быть ']'
    assert text[-1].strip() == "]"
    # Проверяем, что ключи внутри объектов отсортированы
    obj = json.loads("\n".join(text))[1]
    assert list(obj.keys()) == sorted(obj.keys())
