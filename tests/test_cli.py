import subprocess
import sys
from pathlib import Path

import gendiff.scripts.gendiff as cli


def test_build_parser_specs():
    parser = cli.build_parser()
    args = parser.parse_args(["one.json", "two.json"])
    assert args.format == "stylish"


def test_cli_output(tmp_path: Path):
    fixtures = Path(__file__).parent / "fixtures"
    file1 = fixtures / "file1.json"
    file2 = fixtures / "file2.json"

    result = subprocess.run(
        [sys.executable, "-m", "gendiff.scripts.gendiff", file1, file2],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()

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
    assert result == expected
