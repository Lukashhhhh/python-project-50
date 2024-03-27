from gendiff import generate_diff
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish',
        choices=['stylish', 'plain', 'json'],
    )

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def main():
    arguments = get_arguments()
    print(generate_diff(*arguments))


if __name__ == '__main__':
    main()
