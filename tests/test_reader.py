from pathlib import Path

from gendiff import read_file


def test_read_json_files(tmp_path: Path):
    fixtures = Path(__file__).parent / "fixtures"
    file1 = fixtures / "file1.json"
    file2 = fixtures / "file2.json"

    data1 = read_file(file1)
    data2 = read_file(file2)

    assert data1["host"] == data2["host"] == "hexlet.io"
    assert "proxy" in data1 and "proxy" not in data2
    assert data1["timeout"] == 50 and data2["timeout"] == 20
