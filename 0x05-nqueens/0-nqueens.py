#!/usr/bin/python3
"""
NQueens puzzle solver
"""


import sys


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if (sys.argv[1]).isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)


def approve_placment(chessboard, row, col, N):
    
    for i in range(col):
        if chessboard[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if chessboard[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if chessboard[i][j] == 1:
            return False

    return True


def soln(chessboard, col, N):

    if col == N:
        position_of_queens(chessboard)
        return True

    F = False
    for i in range(N):
        if approve_placment(chessboard, i, col, N):
            chessboard[i][col] = 1
            F = soln(chessboard, col + 1, N) or F
            chessboard[i][col] = 0
    return F


def position_of_queens(chessboard):


    positions = []
    for i in range(len(chessboard)):
        for j in range(len(chessboard)):
            if chessboard[i][j] == 1:
                positions.append([i, j])
    print(positions)


chessboard = [[0 for i in range(N)] for j in range(N)]
soln(chessboard, 0, N)
