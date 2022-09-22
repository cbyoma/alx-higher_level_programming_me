#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    get_number = len(sys.argv) - 1

    if get_number == 0:
        print("0 arguments.")
    elif get_number == 1:
        print("1 argument:")
    else:
        print(f"{get_number} arguments:")

    for i in range(get_number):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
