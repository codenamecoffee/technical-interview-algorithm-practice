"""
### Staircase

Given a positive integer n, print a right-aligned staircase of height and width n using the '#' character. 
Each line of the staircase should be right-aligned, with spaces preceding the '#' symbols except for the last line, 
which contains no leading spaces.

The task is inspired by a classic HackerRank challenge, but the description here is adapted for educational purposes.

Parameters:

* n (int): The size of the staircase (height and width).

Output:

* Prints the staircase pattern to standard output. No return value.

Constraints:

* 0 < n <= 100

Example:
Input:
6

Output:
     #
    ##
   ###
  ####
 #####
######

"""

# Solution

def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
        print_content = "#" * i
        spaces = " " * (n - i)
        print(spaces + print_content)
        
        
if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)

"""
### Solution Overview

This implementation uses Python's string multiplication to efficiently create each line of the staircase.
The approach is straightforward: for each row, print (n - i) spaces followed by i '#' characters.
This guarantees right alignment and meets the problem's constraints.
The code is concise, readable, and leverages Python's strengths for simple pattern generation.
¿Te gustaría que agregue este comentario al inicio d

"""