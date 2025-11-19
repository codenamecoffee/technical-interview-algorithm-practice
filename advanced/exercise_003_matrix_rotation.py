"""
Matrix Rotation (90° clockwise)

Concepts: matrix manipulation, indexes, symmetries

Statement

Rotate an NxN matrix 90 degrees clockwise.

Input:

[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

Output:

[
 [7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]
]
"""

matrix_two = [ [1,2], 
               [3,4] ]
"""
 Output:

 matrix_two = [ [3,1], 
                [4,2] ]

"""

matrix_three = [ [1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9] ]



def matrix_rotate(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    if (n == 1): 
        return matrix
    else:
        result = [[] for _ in range(n)]
        for row in range(n): 
            for col in range(n): 
                result[col].insert(0,matrix[row][col])
        return result
            
print(matrix_rotate(matrix_two))
print(matrix_rotate(matrix_three))


"""
Notes:
- The function rotates an NxN matrix 90 degrees clockwise by building a new matrix.
- It initializes 'result' as a list of n empty lists, one for each column in the original matrix.
- For each element in the original matrix, it inserts the value at the beginning of the corresponding row in 'result'.
- This approach works for any NxN matrix and avoids index errors by iterating over column indices (not values).
- The use of 'insert(0, ...)' ensures that elements are placed in the correct order for the rotation.
- The function handles the edge case of a 1x1 matrix by returning it unchanged.
- Time complexity is O(n^2), where n is the size of the matrix.
"""