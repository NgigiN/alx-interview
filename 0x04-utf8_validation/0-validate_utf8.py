#!/usr/bin/python3
"""
    Script to check if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Function to check if a given data set represents a valid UTF-8 encoding
    """
    # Initialize variables
    n = len(data)
    i = 0

    while i < n:
        # Gets the number of bytes needed for the current character
        num_bytes = 1 if (data[i] >> 7) == 0 else (
            (data[i] >> 5) & 0b11111) + 1

        # Checks if there are enough bytes for the current character
        if i + num_bytes > n or num_bytes > 4:
            return False

        # Checks if the following bytes start with 10
        for j in range(1, num_bytes):
            if (data[i+j] >> 6) != 0b10:
                return False

        # Moves to the next character
        i += num_bytes

    return True
