#!/usr/bin/python3

"""
Function to find the least amount of operations to produce a number n
of characters
"""


def minOperations(n):
    """
    Parameters:
    n: operations to be done
    Returns:
    least amount of operations to produce n characters
    if n is impossible just return 0"""
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    stage = 0
    while current_length < n:
        if n % current_length == 0:
            stage = current_length
            operations += 1

        current_length += stage
        operations += 1
    return operations
