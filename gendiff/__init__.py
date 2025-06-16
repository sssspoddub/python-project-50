from gendiff.formatters import choose
from gendiff.parsers import parse
from gendiff.readers import read_file
from gendiff.tree import build_diff

__all__ = ["generate_diff", "read_file"]


def generate_diff(first, second, format_name: str = "stylish") -> str:
    data1 = parse(read_file(first))
    data2 = parse(read_file(second))
    tree = build_diff(data1, data2)
    formatter = choose(format_name)
    return formatter(tree)
