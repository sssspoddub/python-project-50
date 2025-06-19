import pytest

from gendiff.formatters import choose


def test_choose_known_formatters():
    assert callable(choose("stylish"))
    assert callable(choose("plain"))


@pytest.mark.parametrize("bad_name", ["xml", "", "jsonn"])
def test_choose_unknown_formatters_raises(bad_name):
    with pytest.raises(ValueError) as exc:
        choose(bad_name)
    assert f"Unknown format: {bad_name}" in str(exc.value)
