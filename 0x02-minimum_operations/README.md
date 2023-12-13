MinOperations for H characters
Problem:
In a text file, there is a single character H. The text editor can execute only two operations: Copy All and Paste. Given a number 'n', the task is to calculate the fewest number of operations needed to result in exactly 'n' H characters in the file.

Logic
The solution uses a loop to simulate the operations. It maintains a current_length variable representing the current length of the file's content. The loop performs copy all and paste operations based on the value of current_length and checks if 'n' is evenly divisible by current_length. If it is divisible, a copy all operation is performed, updating the stage. The loop continues until the current_length reaches or exceeds 'n', at which point the total number of operations is returned.

Example
n = 12
result = minOperations(n)
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

Output
Min # of operations to reach 12 char: 7

