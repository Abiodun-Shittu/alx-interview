#!/usr/bin/python3
"""
The N queens puzzle
"""
import sys


def is_safe(board, row, col):
    # Check if it is safe to place a queen at board[row][col]
    n = len(board)

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    n = len(board)

    # Base case: If all queens are placed, print the solution
    if col == n:
        print_solution(board)
        return

    # Recursive backtracking:
    # Try placing a queen in each row of the current column
    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, col + 1)
            board[row][col] = 0


def print_solution(board):
    n = len(board)
    solution = []
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i][j] == 1:
                row += "Q "
            else:
                row += ". "
        solution.append(row.strip())
    print("\n".join(solution))
    print()


if __name__ == "__main__":
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [[0] * N for _ in range(N)]

    # Solve the N queens problem
    solve_nqueens(board, 0)
