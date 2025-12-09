"""
Diagonal Difference — Based on a HackerRank Challenge

Given a square matrix, the task is to compute the absolute difference between the sums 
of its two main diagonals.

* The primary diagonal runs from the top-left to the bottom-right.
* The secondary diagonal runs from the top-right to the bottom-left.

Your function should read an n x n matrix and return:

  |sum(primary_diagonal) − sum(secondary_diagonal)|

This is a simple matrix traversal exercise, commonly used to practice indexing, 
iteration, and basic array manipulation.
  
----

Example

For the following matrix:

1 2 3
4 5 6
9 8 9

* Primary diagonal: 1 + 5 + 9 = 15

* Secondary diagonal: 3 + 5 + 9 = 17

* Absolute difference: |15 − 17| = 2

"""

# Solution 1:

def diagonalDifference(arr):
    # Write your code here
    left_to_right = []
    right_to_left = []
    
    pointer_1 = 0
    pointer_2 = len(arr) - 1
    for i in range(len(arr)):
        left_to_right.append(arr[pointer_1][i])
        right_to_left.append(arr[pointer_2][i])
        pointer_1 += 1
        pointer_2 -= 1
        
    print(f"Diagonal izquierda: {left_to_right}")
    print(f"Diagonal derecha: {right_to_left}")
                
    return abs(sum(left_to_right) - sum(right_to_left))


# Solution 2:

def diagonalDifference(arr):
    n = len(arr)
    
    primary = [arr[i][i] for i in range(n)]
    secondary = [arr[i][n - 1 - i] for i in range(n)]
    
    return abs(sum(primary) - sum(secondary))

"""
* We use list comprehensions to traverse both diagonals.

* Manual pointers (pointer_1, pointer_2) are eliminated, since the diagonals follow simple patterns.

* This solution remains 100% equivalent in time and complexity, just more idiomatic.

"""
