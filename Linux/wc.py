#!/usr/bin/python3
import argparse


def wc(command: str, file_name):
    count = 0
    try:
        with open(file_name, 'rt', encoding='utf-8') as f:
            if command == 'chars':
                for line in f:
                    count += len(line)

            elif command == 'words':
                words = []
                for line in f:
                    words.extend(line.split(' '))
                words = list(filter(lambda word: word != '\n', words))
                count = len(words)

            elif command == 'lines':
                count = len(f.readlines())

        return count
    except:
        print('No such file')
        return False


def main():
    parser = argparse.ArgumentParser(description='print newline, word, or byte counts a file')
    parser.add_argument('filename', type=str, help="File's content to count")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-m', '--chars', action='store_true', help='print the character count')
    group.add_argument('-w', '--words', action='store_true', help='print the word count')
    group.add_argument('-l', '--lines', action='store_true', help='print the line count')
    parser.add_argument('-s', '--save', action='store_true', help='save the result in file')
    args = parser.parse_args()

    command = ''
    if args.chars:
        command = 'chars'
    elif args.words:
        command = 'words'
    elif args.lines:
        command = 'lines'

    result = wc(command, args.filename)

    if args.save:
        try:
            with open('wc_result.txt', 'a') as f:
                f.write(f'{args.filename}: {result} {command}\n')
        except:
            print('File error')
            return False
    print(result)


if __name__ == '__main__':
    main()
