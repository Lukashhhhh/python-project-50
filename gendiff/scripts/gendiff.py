from gendiff import generate_diff
import argparse


FORMAT_LIST = ['stylish', 'plain', 'json']


def check_format(format):
    if format not in FORMAT_LIST:
        print('You have entered an incorrect format. '
              'Output in default format')
        return 'stylish'
    return format


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish',
        choices=FORMAT_LIST,
        type=check_format
    )

    args = parser.parse_args()
    print(
        generate_diff(args.first_file, args.second_file, args.format)
    )


if __name__ == '__main__':
    main()
