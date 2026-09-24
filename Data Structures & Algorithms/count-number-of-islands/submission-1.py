class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        numIslands = 0

        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            
            # If out of bounds or visited or not an island
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == "0"):
                return
            
            visit.add((r,c))
            dfs(grid, r + 1, c, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r, c - 1, visit)
            dfs(grid, r, c + 1, visit)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visit:
                    numIslands += 1
                    dfs(grid, row, col, visit)

        return numIslands