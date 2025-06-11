import json
import yaml
from pathlib import Path


def load_file(filepath):
    filepath = Path(filepath)
    if filepath.suffix in ['.json']:
        with open(filepath) as f:
            return json.load(f)
    if filepath.suffix in ['.yml', '.yaml']:
        with open(filepath) as f:
            return yaml.safe_load(f)
    raise ValueError(f'Unsupported file format: {filepath.suffix}')


def build_diff(filepath1, filepath2):
    data1 = load_file(filepath1)
    data2 = load_file(filepath2)

    def diff_dict(d1, d2):
        keys = sorted(set(d1.keys()) | set(d2.keys()))
        result = []
        for key in keys:
            if key not in d1:
                result.append(
                    {'key': key, 'status': 'added', 'value': d2[key]})
            elif key not in d2:
                result.append(
                    {'key': key, 'status': 'removed', 'value': d1[key]})
            else:
                val1 = d1[key]
                val2 = d2[key]
                if isinstance(val1, dict) and isinstance(val2, dict):
                    children = diff_dict(val1, val2)
                    result.append(
                        {'key': key, 'status': 'nested', 'children': children})
                elif val1 == val2:
                    result.append(
                        {'key': key, 'status': 'unchanged', 'value': val1})
                else:
                    result.append(
                        {'key': key, 'status': 'changed', 'old_value': val1,
                            'new_value': val2})
        return result

    return diff_dict(data1, data2)
