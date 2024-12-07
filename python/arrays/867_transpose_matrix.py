from typing import List


# traspose matrix tc: o(n^2)
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    r = len(matrix)
    c = len(matrix[0])

    output = [
        [0 for _ in range(r)] for _ in range(c)
    ]  # this is required becase assigning to location that doesnot exist will give index error.

    for i in range(0, r):
        for j in range(0, c):
            output[j][i] = matrix[i][j]

    print(output)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose(matrix)
