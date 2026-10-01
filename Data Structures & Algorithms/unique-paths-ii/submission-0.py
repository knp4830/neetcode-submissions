class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        prevRow = [0] * n
        prevRow[n - 1] = 1

        for r in range(m - 1, - 1, -1):
            curRow = [0] * n
            curRow[n - 1] = prevRow[n - 1] if obstacleGrid[r][n-1] == 0 else 0
            for c in range(n - 2, -1, -1):
                curRow[c] = (curRow[c + 1] + prevRow[c]) if obstacleGrid[r][c] == 0 else 0
            prevRow = curRow

        return prevRow[0]