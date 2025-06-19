import pytest

from gendiff.formatters import choose
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


@pytest.mark.parametrize(
    "name, expected",
    [
        ("plain", format_plain),
        ("stylish", format_stylish),
        ("json", format_json),
    ],
)
def test_choose_known(name, expected):
    assert choose(name) is expected


def test_choose_unknown():
    with pytest.raises(ValueError) as exc:
        choose("no-such-format")
    assert "Unknown format: no-such-format" in str(exc.value)
