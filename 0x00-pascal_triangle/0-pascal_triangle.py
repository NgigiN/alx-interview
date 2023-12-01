#!/usr/bin/python3
"""
function that returns a list of integers representing a pascal
triangle of n
"""


def pascal_triangle(n):
    """
    Prints the triangle of Pascal
    Assumption: returns empty in n<= 0
                n will always be an integer
    """
    result = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(row)
    return result
