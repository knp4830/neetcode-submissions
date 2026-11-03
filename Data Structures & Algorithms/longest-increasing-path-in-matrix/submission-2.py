class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            res = 1                                        # the cell by itself
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0 or nr == ROWS or nc == COLS
                        or matrix[nr][nc] <= matrix[r][c]):   # out of bounds or not bigger
                    continue
                res = max(res, 1 + dfs(nr, nc))

            memo[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
        return max(memo.values())