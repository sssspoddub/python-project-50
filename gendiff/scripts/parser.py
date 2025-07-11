import json
from pathlib import Path

import yaml


def parse_file(path):
    ext = Path(path).suffix.lower()

    with open(path, 'r') as f:
        if ext in ('.yaml', '.yml'):
            return yaml.safe_load(f)
        elif ext == '.json':
            return json.load(f)
        else:
            raise ValueError(f'Unsupported file format: {ext}')
