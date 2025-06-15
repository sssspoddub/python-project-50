from pathlib import Path

from gendiff import read_file


def test_read_json_files():
    fixtures = Path(__file__).parent / "fixtures"
    file1 = fixtures / "file1.json"
    file2 = fixtures / "file2.json"

    data1 = read_file(file1)
    data2 = read_file(file2)

    # file1.json
    assert data1 == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
    }

    # file2.json
    assert data2 == {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io",
    }
