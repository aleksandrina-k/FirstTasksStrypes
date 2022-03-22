import sys


def cat(file_name: str):
    try:
        with open(file_name, 'rt', encoding='utf-8') as f:
            for line in f:
                print(line.strip('\n'))
            print()
    except:
        print('No such file')
        return False


def main():
    for arg in sys.argv[1:]:
        cat(str(arg))


if __name__ == '__main__':
    main()
