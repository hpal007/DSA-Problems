"""
Rotate Matrix/ Image - LeetCode 48
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
Example:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

"""

import numpy as np

# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # this make rows to cols inplace 
    
    for el in matrix:
        # el.reverse()
        el[:] = el[::-1]  # this reverse each row inplace
    
rotate(matrix)
print(matrix)
