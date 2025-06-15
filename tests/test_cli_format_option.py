import json
from pathlib import Path

import pytest

from gendiff.scripts.gendiff import build_parser, main


def _tmp_json(tmp_path: Path, data: dict, name: str) -> Path:
    f = tmp_path / name
    f.write_text(json.dumps(data))
    return f


@pytest.mark.parametrize(
    ("file1", "file2"),
    [
        ("tests/fixtures/file1.json", "tests/fixtures/file2.json"),
        ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml"),
    ],
    ids=["json", "yaml"],
)
@pytest.mark.parametrize(
    "opt",
    [[], ["-f", "stylish"], ["--format", "stylish"]],
    ids=["no-flag", "-f", "--format"],
)
def test_cli_formats(tmp_path, capsys, file1, file2, opt):
    main([*opt, file1, file2])
    out = capsys.readouterr().out.strip()
    assert "- proxy:" in out or "- follow:" in out


def test_parser_rejects_unknown_format():
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--format", "xml", "a", "b"])
