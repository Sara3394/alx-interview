#!/usr/bin/python3
'''
N Queen Puzzle Solver

'''


import sys


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if (sys.argv[1]).isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)


def approve_placment(chessboard, row, col, Q): 

    for i in range(col):
        if chessboard[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if chessboard[i][j] == 1:
            return False

    for i, j in zip(range(row, Q, 1),
                    range(col, -1, -1)):
        if chessboard[i][j] == 1:
            return False

    return True


def Soln(chessboard, col, Q):


    if col == Q:
        Position_of_queens(chessboard)
        return True

    for i in range(Q):
        if approve_placment(chessboard, i, col, Q):
            chessboard[i][col] = 1
            False = Soln(chessboard, col + 1, Q) or False
            chessboard[i][col] = 0
    return False


def Position_of_queens(chessboard):


    positions = []
    for i in range(len(chessboard)):
        for j in range(len(chessboard)):
            if chessboard[i][j] == 1:
                positions.append([i, j])
    print(positions)


chessboard = [[0 for i in range(Q)] for j in range(Q)]
Soln(chessboard, 0, Q)
