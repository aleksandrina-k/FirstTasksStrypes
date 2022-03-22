import sys
from random import randint


def generate_numbers(file_name, numbers):
    with open(file_name, 'wt') as f:
        content = []
        for _ in range(numbers):
            content.append(str(randint(1, 1000)))
        f.write(' '.join(content)+'\n')


def main():
    file_name = sys.argv[1]
    number = int(sys.argv[2])
    generate_numbers(file_name, number)


if __name__ == '__main__':
    main()
