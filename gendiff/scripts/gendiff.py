from __future__ import annotations

import sys
from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path

from gendiff import generate_diff

_AVAILABLE_FORMATS: tuple[str, ...] = ("stylish", "plain", "json")


def _format_type(value: str) -> str:
    if value not in _AVAILABLE_FORMATS:
        raise ArgumentTypeError(f"unknown format: {value!r}")
    return value


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=_format_type,
        metavar="FORMAT",
        default="stylish",
        help="set format of output",
    )
    parser.add_argument("first_file", type=Path)
    parser.add_argument("second_file", type=Path)
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    diff = generate_diff(args.first_file, args.second_file, args.format)
    sys.stdout.write(f"{diff}\n")


if __name__ == "__main__":
    main()
