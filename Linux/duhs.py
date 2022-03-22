import os
import sys


def duhs(path):
    total_size = 0
    try:
        for p in os.listdir(path):
            full_path = os.path.join(path, p)

            if os.path.isfile(full_path):
                var = os.path.getsize(full_path)
                print(f"{var} {full_path}")
                total_size += var
            elif os.path.isdir(full_path):
                var = duhs(full_path)
                print(f"{var} {full_path}")
                total_size += var
        return total_size

    except OSError:
        print('Wrong path')
        return False


def main():
    print(duhs(sys.argv[1]))
    #path = "C:\\Users\\Aleks Karadalieva\\Desktop\\projects"
    #print(duhs(path))


if __name__ == '__main__':
    main()
