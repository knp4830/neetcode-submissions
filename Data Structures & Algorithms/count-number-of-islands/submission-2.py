class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL, count = len(grid), len(grid[0]), 0
        visit = set()
        def dfs(r, c):
            if (min(r, c) < 0 or r == ROW or c == COL or (r,c) in visit or grid[r][c] == "0"):
                return
            
            visit.add((r,c))

            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visit and grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        
        return count
                