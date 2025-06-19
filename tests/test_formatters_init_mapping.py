import pytest

from gendiff.formatters import choose
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


@pytest.mark.parametrize(
    "name, func",
    [
        ("plain", format_plain),
        ("stylish", format_stylish),
        ("json", format_json),
    ],
)
def test_choose_all_known(name, func):
    """Проверяем, что mapping в __init__.py включает все три формата."""
    assert choose(name) is func


def test_choose_unknown_format_raises():
    with pytest.raises(ValueError) as exc:
        choose("xml")
    assert "Unknown format: xml" in str(exc.value)
