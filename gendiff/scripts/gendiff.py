import argparse

from gendiff.scripts.core import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file',
                        help='Path to the first configuration file')
    parser.add_argument('second_file',
                        help='Path to the second configuration file')
    parser.add_argument('-f', '--format', metavar='FORMAT', default='stylish',
                        help='set format of output (default: stylish)')

    args = parser.parse_args()

    print(generate_diff(args.first_file,
                        args.second_file,
                        format_name=args.format))


if __name__ == '__main__':
    main()
