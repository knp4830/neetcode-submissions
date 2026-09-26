class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Review
        # Using a little matrix math we can transpose and transform
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Transform
        for i in range(n):
            matrix[i].reverse()
