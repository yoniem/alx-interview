#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.
    
    Args:
        matrix (list of list of int): 2D matrix to rotate
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
