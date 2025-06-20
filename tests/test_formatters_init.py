import pytest

from gendiff.formatters import choose
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def test_choose_returns_correct_formatter():
    assert choose("plain") is format_plain
    assert choose("stylish") is format_stylish
    assert choose("json") is format_json


def test_choose_raises_for_unknown():
    with pytest.raises(ValueError) as exc:
        choose("xml")
    assert "Unknown format" in str(exc.value)
