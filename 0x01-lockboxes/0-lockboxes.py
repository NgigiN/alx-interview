#!/usr/bin/python3
"""
Interview question solution on the lock boxes problem
"""


def canUnlockAll(boxes):
    n = len(boxes)
    item = [False] * n
    item[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for each in boxes[box]:
            if each >= 0 and each < n and not item[each]:
                item[each] = True
                stack.append(each)

    return all(item)
