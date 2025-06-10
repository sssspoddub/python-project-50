import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        default='stylish',
        help='set format of output'
    )
    args = parser.parse_args()
    data1 = read_file(args.first_file)
    data2 = read_file(args.second_file)
    print(data1)
    print(data2)


def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
