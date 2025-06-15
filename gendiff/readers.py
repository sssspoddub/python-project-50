"""Чтение и парсинг конфигурационных файлов.

Пока поддерживается только JSON. Позже сюда добавятся YAML / TOML-парсеры.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


def read_file(path: str | Path) -> Mapping[str, Any]:
    """Прочитать конфигурационный файл и вернуть данные как словарь.

    Поддерживаемые расширения:
        • .json  – парсится через json.load()

    Args:
        path: путь до файла.

    Returns:
        Parsed data (dict-like).

    Raises:
        ValueError: если формат не поддерживается.
        OSError:    если файл не найден (прилетают системные исключения).
        json.JSONDecodeError: неверный JSON.
    """
    path = Path(path)
    if path.suffix.lower() == ".json":
        with path.open(encoding="utf-8") as fd:
            return json.load(fd)

    raise ValueError(f"Unsupported file format: {path.suffix!r}")
