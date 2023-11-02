#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    result = 0
    arguments = len(argv)
    for args in range(arguments - 1):
        result += int(argv[args + 1])
    print("{}".format(result))
