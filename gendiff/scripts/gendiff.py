import argparse
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", type=Path)
    parser.add_argument("second_file", type=Path)
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    sys.stdout.write("Feature not implemented yet\n")


if __name__ == "__main__":
    main()
