### Hexlet tests and linter status:
[![Actions Status](https://github.com/sssspoddub/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/sssspoddub/python-project-50/actions)

## Пример использования

```python
from gendiff import generate_diff
from gendiff.scripts.gendiff import read_file

file_path1 = 'file1.json'
file_path2 = 'file2.json'

data1 = read_file(file_path1)
data2 = read_file(file_path2)

diff = generate_diff(data1, data2)
print(diff)
