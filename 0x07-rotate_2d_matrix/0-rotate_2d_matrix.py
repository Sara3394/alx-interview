#!/usr/bin/python3
""" rotate 2D matrix"""


def rotate_2d_matrix(m):
    """ rotates a 2D matrix 90 degrees clockwise
    m: nxn matrix

    """

    n = len(m)
    temp = [row[:] for row in m]
    for i in range(n):
        for j in range(n):
            m[i][j] = temp[n - j - 1][i]
