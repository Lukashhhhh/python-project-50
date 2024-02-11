import argparse


def main():
    gendiff = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    gendiff.add_argument('first_file')
    gendiff.add_argument('second_file')
    gendiff.add_argument('-f', '--format', help='set format of output')

    args = gendiff.parse_args()

if __name__ == '__main__':
    main()