#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in range(len(matrix)):
        for i in range(len(matrix[y])):
            print("{:d}".format(matrix[y][i]), end="")
            if i != (len(matrix[y]) - 1):
                print(" ", end="")

        print("")
