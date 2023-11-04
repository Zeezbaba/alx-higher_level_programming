#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for column in rows:
            if column == row[-1]:
                print('{:d}'.format(column), end='')
            else:
                print('{:d}'.format(column), end=' ')
        print()
