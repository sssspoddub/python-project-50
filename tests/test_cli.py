import importlib
import sys
from pathlib import Path
from subprocess import run, PIPE

import pytest

import gendiff.scripts.gendiff as cli


def test_build_parser_specs():
    parser = cli.build_parser()
    assert parser.prog == "gendiff"
    args = parser.parse_args(["a.json", "b.json"])
    assert isinstance(args.first_file, Path)
    assert isinstance(args.second_file, Path)


def test_help_output(capsys):
    with pytest.raises(SystemExit) as exc:
        cli.build_parser().parse_args(["-h"])
    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert "usage: gendiff" in captured.out
    assert "first_file" in captured.out and "second_file" in captured.out


def test_main_placeholder(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["gendiff", "a.json", "b.json"])
    cli.main()
    out, _ = capsys.readouterr()
    assert out.strip() == "Feature not implemented yet"
