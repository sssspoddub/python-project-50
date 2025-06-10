import json
from .diff import build_diff_dict


def generate_diff(file_path1: str, file_path2: str) -> str:
    with open(file_path1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)
    with open(file_path2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)
    return build_diff_dict(data1, data2)
