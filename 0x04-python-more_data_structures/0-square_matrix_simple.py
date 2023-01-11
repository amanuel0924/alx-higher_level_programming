#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for x in range(len(matrix)):
        new_list.append(list(map((lambda y: y*y), matrix[x])))
    return new_list
