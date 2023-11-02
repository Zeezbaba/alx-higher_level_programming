#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    number_of_args = len(argv) - 1
    if number_of_args == 0:
        print("0 arguments.")
    elif number_of_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number_of_args))
    for i in range(number_of_args):
        print("{}: {}".format(i + 1, argv[i + 1]))
