"""Чтение JSON-/YAML-файлов и отдача dict."""

from pathlib import Path
from typing import Mapping

from gendiff.parsers import parse


def read_file(path: str | Path | Mapping) -> dict:
    """Всегда возвращает dict (для файлов и уже готовых mapping-объектов)."""
    return parse(path)
