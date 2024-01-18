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
        if (data[i] & 0xFF) >> 7 == 0:
            num_bytes = 1
        elif (data[i] & 0xFF) >> 5 == 0b110:
            num_bytes = 2
        elif (data[i] & 0xFF) >> 4 == 0b1110:
            num_bytes = 3
        elif (data[i] & 0xFF) >> 3 == 0b11110:
            num_bytes = 4
        else:
            return False

        if i + num_bytes > n:
            return False

        for j in range(1, num_bytes):
            if (data[i+j] & 0xFF) >> 6 != 0b10:
                return False

        i += num_bytes

    return True
