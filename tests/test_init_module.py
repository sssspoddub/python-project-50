
import pytest

from gendiff import generate_diff

TXT1 = '{"foo": "bar"}'
TXT2 = '{"foo": "baz"}'


def test_generate_diff_default(tmp_path):
    f1 = tmp_path / "1.json"
    f2 = tmp_path / "2.json"
    f1.write_text(TXT1)
    f2.write_text(TXT2)

    diff = generate_diff(str(f1), str(f2))
    assert "foo" in diff
    assert "-" in diff and "+" in diff


def test_generate_diff_unknown_format(tmp_path):
    f1 = tmp_path / "1.json"
    f2 = tmp_path / "2.json"
    f1.write_text(TXT1)
    f2.write_text(TXT2)

    with pytest.raises(ValueError):
        generate_diff(str(f1), str(f2), format_name="nope")
