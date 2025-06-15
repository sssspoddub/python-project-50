from gendiff.formatters.stylish import format_stylish
from gendiff.parsers import parse
from gendiff.readers import read_file
from gendiff.tree import build_diff

__all__ = ["generate_diff", "read_file"]


def generate_diff(first, second, format_name: str = "stylish") -> str:  # noqa: D401
    """
    Построить diff между двумя файлами/словорами.

    Parameters
    ----------
    first, second : str | Mapping
        Пути к файлам или уже разобранные структуры.
    format_name : str, default ``"stylish"``
        Имя выходного форматтера.

    Returns
    -------
    str
        Строка с человеко-читаемым diff.
    """
    data1 = parse(first)
    data2 = parse(second)
    tree = build_diff(data1, data2)

    if format_name == "stylish":
        return format_stylish(tree)

    raise ValueError(f"unknown format: {format_name}")
