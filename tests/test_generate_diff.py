from pathlib import Path

from gendiff import generate_diff


def test_generate_diff(tmp_path: Path):
    fixtures = Path(__file__).parent / "fixtures"
    file1 = fixtures / "file1.json"
    file2 = fixtures / "file2.json"

    expected = (
        "{\n"
        "  - follow: false\n"
        "    host: hexlet.io\n"
        "  - proxy: 123.234.53.22\n"
        "  - timeout: 50\n"
        "  + timeout: 20\n"
        "  + verbose: true\n"
        "}"
    )
    assert generate_diff(file1, file2) == expected
