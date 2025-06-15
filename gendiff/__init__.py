from gendiff.formatters.stylish import format_stylish
from gendiff.parsers import parse
from gendiff.readers import read_file
from gendiff.tree import build_diff

__all__ = ["generate_diff", "read_file"]


def generate_diff(first, second, format_name: str = "stylish") -> str:
    """Построить diff между двумя файлами/словарами и отформатировать его.

    Args:
        first: Путь к первому файлу или уже разобранный dict.
        second: Путь ко второму файлу или уже разобранный dict.
        format_name: Имя форматтера вывода (по умолчанию ``stylish``).

    Returns:
        Строка с результатом сравнения.

    Raises:
        ValueError: Если указан неизвестный формат вывода.
    """
    data1 = parse(first)
    data2 = parse(second)
    tree = build_diff(data1, data2)

    if format_name == "stylish":
        return format_stylish(tree)

    raise ValueError(f"unknown format: {format_name}")
