class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Traditional version
        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r,c, prevVal):
            if (min(r,c ) < 0 or r == rows or c == cols or matrix[r][c] <= prevVal):
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            
            res = 1 + max(dfs(r + 1, c, matrix[r][c]),
                        dfs(r - 1, c, matrix[r][c]),
                        dfs(r, c + 1, matrix[r][c]),
                        dfs(r, c - 1 , matrix[r][c]))

            memo[(r,c)] = res
            return res

        return max(dfs(r, c, -1) for r in range(rows) for c in range(cols))
            