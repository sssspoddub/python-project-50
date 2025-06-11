import json
import os

import yaml


def parse_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    with open(filepath) as f:
        if ext in ['.yml', '.yaml']:
            return yaml.safe_load(f)
        elif ext == '.json':
            return json.load(f)
        else:
            raise ValueError(f"Unsupported file format: {ext}")
