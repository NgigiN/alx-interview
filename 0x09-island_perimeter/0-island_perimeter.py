#!/usr/bin/python3

"""
returns the area of a grid
"""


def island_perimeter(grid):
    """
    finds the perimeter of the island
    1: is land
    0: is water
    Each cell is a square with side length 1
    Cells are connected horizontally/vertically (not diagonally)
    grid is rectangular, width and height don't exceed 100

    Parameters
    grid: is a list of list of integers either 1 or 0

    Returns
    perimerter of the island
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
