#!/usr/bin/python3
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    return [[' ' for _ in range(n)] for _ in range(n)]


def is_safe(board, row, col):
    """Check if placing a queen at a given position is safe."""
    for i in range(row):
        if board[i][col] == 'Q' or \
           (col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q') or \
           (col + (row - i) < len(board) and board[i][col + (row - i)] == 'Q'):
            return False
    return True


def recursive_solve(board, row, solutions):
    """Recursively solve an N-queens puzzle."""
    if row == len(board):
        solutions.append([pos[:] for pos in board])
        return solutions

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            solutions = recursive_solve(board, row + 1, solutions)
            board[row][col] = ' '  # backtrack

    return solutions


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 'Q':
                solution.append([r, c])
    return solution


def solve_n_queens(n):
    """Main function to solve the N-queens puzzle."""
    board = init_board(n)
    solutions = recursive_solve(board, 0, [])
    return [get_solution(sol) for sol in solutions]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    if N.isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for sol in solutions:
        print(sol)
