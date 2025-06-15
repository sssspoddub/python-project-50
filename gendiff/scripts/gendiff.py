#!/usr/bin/env python3
"""gendiff – compare two configuration files and show a difference."""

import argparse
import sys
from pathlib import Path

from gendiff import generate_diff


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", type=Path)
    parser.add_argument("second_file", type=Path)
    parser.add_argument(
        "-f", "--format",
        metavar="FORMAT",
        default="stylish",
        help="set format of output",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    diff = generate_diff(args.first_file, args.second_file)
    sys.stdout.write(diff + "\n")


if __name__ == "__main__":
    main()
