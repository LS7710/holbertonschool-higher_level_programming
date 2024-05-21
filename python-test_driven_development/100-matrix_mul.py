#!/usr/bin/python3
"""
This module provides a function 'matrix_mul' to multiply two matrices.
It includes input validation to ensure matrices are correctly formatted for multiplication.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b and returns the resulting matrix.

    Args:
    m_a (list of lists of int/float): The first matrix.
    m_b (list of lists of int/float): The second matrix.

    Raises:
    TypeError: If m_a or m_b are not list of lists, or contain non-integers/floats,
               or if their rows are not of the same size, or they are not lists.
    ValueError: If m_a or m_b are empty or cannot be multiplied due to dimension mismatch.

    Returns:
    list of lists of int/float: The matrix resulting from multiplying m_a by m_b.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if m_a == [] or m_b == [] or m_a == [[]] or m_b == [[]]:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(row, list) for row in m_a + m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if not all(all(isinstance(num, (int, float)) for num in row) for row in m_a + m_b):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if not all(len(m_a[0]) == len(row) for row in m_a) or not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
