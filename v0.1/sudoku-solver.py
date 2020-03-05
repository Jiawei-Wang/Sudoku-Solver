"""
# Brute force sudoku solver (try every possible combination)
# Author: Jiawei Wang
# 3/4/2020
"""


# Find cells without value
def find_empty_cell(Board):
    for row in range(9):
        for col in range(9):
            if Board[row][col] is None:
                return row, col
    return None, None


# Find possible options for Board[row][col]
def get_valid_options(Board, row, col):
    invalid = set([])

    for i in range(9):
        if Board[row][i] is not None:
            invalid.update([Board[row][i]])
        if Board[i][col] is not None:
            invalid.update([Board[i][col]])

    box_row = row - (row % 3)
    box_col = col - (col % 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if Board[i][j] is not None:
                invalid.update([Board[i][j]])

    return set(range(1, 10)) - invalid


# Check whether the board has been filled or not
def solve_sudoku(Board):
    row, col = find_empty_cell(Board)

    if row is None and col is None:
        return True

    valid_options = get_valid_options(Board, row, col)
    for i in valid_options:
        Board[row][col] = i
        if solve_sudoku(Board):
            return True
        Board[row][col] = None

    return False


# Initialize the board
Board = [
    [6, None, 8, 7, None, 2, 1, None, None],
    [4, None, None, None, 1, None, None, None, 2],
    [None, 2, 5, 4, None, None, None, None, None],
    [7, None, 1, None, 8, None, 4, None, 5],
    [None, 8, None, None, None, None, None, 7, None],
    [5, None, 9, None, 6, None, 3, None, 1],
    [None, None, None, None, None, 6, 7, 5, None],
    [2, None, None, None, 9, None, None, None, 8],
    [None, None, 6, 8, None, 5, 2, None, 3]
]

if solve_sudoku(Board):
    for i in range(9):
        print(Board[i])

else:
    print("No Solution found")