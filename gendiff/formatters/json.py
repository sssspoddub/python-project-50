import json
from typing import Dict, List


def format_json(tree: List[Dict]) -> str:
    return json.dumps(tree, indent=4, sort_keys=True)
