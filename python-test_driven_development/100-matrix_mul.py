#!/usr/bin/python3
"""
This module provides a function matrix_mul that multiplies two matrices.
It includes comprehensive input validation according to specified rules.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
    m_a (list of lists of int/float): The first matrix.
    m_b (list of lists of int/float): The second matrix.

    Raises:
    TypeError: If m_a or m_b are not lists of lists, or contain non-integers/floats,
               or if their rows are not of the same size.
    ValueError: If m_a or m_b are empty, or if their dimensions are not compatible for multiplication.

    Returns:
    list of lists of int/float: The resulting matrix from multiplying m_a by m_b.
    """
    def check_matrix(matrix, name):
        if not isinstance(matrix, list):
            raise TypeError(f"{name} must be a list")
        if matrix == [] or matrix == [[]]:
            raise ValueError(f"{name} can't be empty")
        if any(not isinstance(row, list) for row in matrix):
            raise TypeError(f"{name} must be a list of lists")
        if any(not all(isinstance(num, (int, float)) for num in row) for row in matrix):
            raise TypeError(f"{name} should contain only integers or floats")
        if len(set(len(row) for row in matrix)) != 1:
            raise TypeError(f"each row of {name} must be of the same size")

    check_matrix(m_a, "m_a")
    check_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
