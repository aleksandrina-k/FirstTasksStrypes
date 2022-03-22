import sys


def sum_numbers(file_name):
    try:
        with open(file_name, 'rt') as f:
            numbers = f.readlines()
            numbers = numbers[0].strip('\n')
            numbers = [int(x) for x in numbers.split(' ')]

            total_sum = sum(numbers)

            print(total_sum)
    except:
        print('No such file')
        return False


def main():
    sum_numbers(sys.argv[1])


if __name__ == '__main__':
    main()
