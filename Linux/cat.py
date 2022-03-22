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
    cat(sys.argv[1])


if __name__ == '__main__':
    main()
