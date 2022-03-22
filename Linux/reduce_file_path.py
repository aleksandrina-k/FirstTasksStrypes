#!/usr/bin/python3
import os.path
import sys


def reduce_file_path(path):
    directories = path.split('/')
    count_back = directories.count('..')
    directories = list(filter(lambda x: x != '' and x != '.', directories))
    result = []

    for index, dir in enumerate(directories):
        if dir != '..':
            result.append(dir)
        else:
            result.pop(-1)

    # while 0 < count_back <= len(directories) and len(directories) > 0:
    #     directories.pop(-1)
    #     count_back -= 1

    return '/' + '/'.join(result)


def main():
    path = sys.argv[1]
    print(reduce_file_path(path))


if __name__ == '__main__':
    main()
