#!/usr/bin/python3
"""
mod 12
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of height n.

    Args:
        n (int): The number of levels of the triangle to generate.

    Returns:
        List of lists of integers representing Pascal's triangle.
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
