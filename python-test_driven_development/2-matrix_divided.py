#!/usr/bin/python3
"""
This module provides a function matrix_divided that divides all elements of a matrix by a divisor.
The function ensures that the matrix is properly formatted and the division operations are valid.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and rounds the results to 2 decimal places.

    Args:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The divisor.

    Raises:
    TypeError: If the matrix is not a list of lists of integers/floats,
               if the rows are not all the same size, or if div is not a number.
    ValueError: If div is zero.

    Returns:
    list of lists of float: A new matrix with the division results.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
