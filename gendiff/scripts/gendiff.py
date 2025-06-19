import sys
from argparse import ArgumentParser
from pathlib import Path

from gendiff import generate_diff

_AVAILABLE_FORMATS = ["stylish", "plain", "json"]


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument(
        "-f",
        "--format",
        choices=_AVAILABLE_FORMATS,
        default="stylish",
        help="set format of output",
    )
    parser.add_argument("first_file", type=Path)
    parser.add_argument("second_file", type=Path)
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    diff = generate_diff(args.first_file, args.second_file, args.format)
    sys.stdout.write(f"{diff}\n")


if __name__ == "__main__":
    main()
