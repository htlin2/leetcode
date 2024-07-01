class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        matrix[:] = zip(*matrix)
        # reverse row
        for i in range(len(matrix)):
            matrix[i] = reversed(matrix[i])

"""
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transpose
[
    [1,4,7],
    [2,5,8],
    [3,6,9]
]
reverse rows
[
    [7,4,1],
    [8,5,2],
    [9,6,3]
]
Output: [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]

"""