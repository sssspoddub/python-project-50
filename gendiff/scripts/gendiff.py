import sys
from argparse import ArgumentParser
from pathlib import Path

from gendiff.diff import generate_diff


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", type=Path)
    parser.add_argument("second_file", type=Path)
    parser.add_argument(
        "-f",
        "--format",
        metavar="FORMAT",
        default="stylish",
        choices=["stylish"],
        help="set format of output",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    diff = generate_diff(args.first_file, args.second_file, fmt=args.format)
    sys.stdout.write(f"{diff}\n")


if __name__ == "__main__":
    main()
