import sys
from pathlib import Path

import pytest

import gendiff.scripts.gendiff as cli


def test_build_parser_specs():
    parser = cli.build_parser()
    assert parser.prog == "gendiff"
    args = parser.parse_args(["file1", "file2"])
    assert isinstance(args.first_file, Path)
    assert isinstance(args.second_file, Path)
    assert args.format == "stylish"  # default value


def test_format_option_parsed():
    parser = cli.build_parser()
    args = parser.parse_args(["-f", "plain", "a.txt", "b.txt"])
    assert args.format == "plain"


def test_help_contains_format(capsys):
    with pytest.raises(SystemExit):
        cli.build_parser().parse_args(["--help"])
    out, _ = capsys.readouterr()
    assert "-f FORMAT, --format FORMAT" in out


def test_main_placeholder(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["gendiff", "one", "two"])
    cli.main()
    out, _ = capsys.readouterr()
    assert out.strip() == "Feature not implemented yet"
