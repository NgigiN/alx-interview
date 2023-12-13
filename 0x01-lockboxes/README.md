Overview
The Box Unlocker module is a Python script that determines if all boxes can be opened given a list of keys. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to other boxes. A key with the same number as a box opens that box. The first box is always unlocked.

Parameters:
boxes(list of lists): A list of lists where each sub-list represents the keys in a box

Assumptions and Constraints
All keys will be positive integers.
There can be keys that do not have boxes.
The first box boxes[0] is always unlocked.

Returns True if all boxes can be opened, else return False


Solution:
This solution uses a depth-first seach algorithm to expolre all possible paths and determine if all boxes can be opened.