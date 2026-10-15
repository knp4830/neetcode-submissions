class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxArea = 0
        # Helper DFS
        def dfs(r, c):
            if (min(r,c) < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == 0):
                return 0
            
            # If it is a 1 add it and we want to continue searching
            visit.add((r,c))

            count = 1
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea

            

