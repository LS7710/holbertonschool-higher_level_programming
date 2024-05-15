#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Compute the square of each element in a 2D matrix.

    Args:
    matrix (list of list of int): The input 2D matrix.

    Returns:
    list of list of int: A new matrix where each element is the square of the element from the input matrix.
    """
    return [[x**2 for x in row] for row in matrix]
