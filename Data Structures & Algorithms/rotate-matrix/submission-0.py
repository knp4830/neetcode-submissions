class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # We tranpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # We reverse
        for i in range(n):
            matrix[i].reverse()