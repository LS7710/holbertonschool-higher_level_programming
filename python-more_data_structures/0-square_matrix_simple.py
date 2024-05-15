#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None or not matrix:
        return []
    
    new_matrix = []
    for row in matrix:
        new_matrix.append([x**2 for x in row])
    
    return new_matrix

