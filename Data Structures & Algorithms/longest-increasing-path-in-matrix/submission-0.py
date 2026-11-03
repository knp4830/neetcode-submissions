class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        memo = {} # Key = (r,c), value = longest path

        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            
            best = 1
            for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            memo[(r,c)] = best
            return best

        return max(dfs(r,c) for r in range(row) for c in range(col))