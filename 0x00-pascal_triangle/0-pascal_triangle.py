#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
    - n: An integer representing the number of rows to generate.

    Returns:
    - A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's Triangle

    for i in range(1, n):
        row = [1]  # Start each row with the number 1
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with the number 1
        triangle.append(row)

    return triangle
