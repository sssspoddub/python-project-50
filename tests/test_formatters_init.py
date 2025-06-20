import pytest

from gendiff.formatters import choose
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def test_choose_known():
    assert choose("json") is format_json
    assert choose("plain") is format_plain
    assert choose("stylish") is format_stylish


def test_choose_unknown():
    with pytest.raises(ValueError) as exc:
        choose("foobar")
    assert "Unknown format: foobar" in str(exc.value)
