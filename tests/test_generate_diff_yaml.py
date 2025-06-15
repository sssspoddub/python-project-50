from pathlib import Path

from gendiff.diff import generate_diff


def test_generate_diff_yaml():
    f1 = Path("tests/fixtures/file1.yml")
    f2 = Path("tests/fixtures/file2.yml")

    expected = (
        "{\n"
        "  - follow: False\n"
        "    host: hexlet.io\n"
        "  - proxy: 123.234.53.22\n"
        "  - timeout: 50\n"
        "  + timeout: 20\n"
        "  + verbose: True\n"
        "}"
    )
    assert generate_diff(f1, f2) == expected
