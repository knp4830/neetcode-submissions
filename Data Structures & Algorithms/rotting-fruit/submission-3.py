class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0]) # Boundaries
        visit = set()                       # don't run into each other
        fresh = time = 0                    # you want to check how many fresh fruit there are, and time is the output
        q = deque()

        # We want to initialize our BFS with all the values
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    visit.add((r,c))
                    q.append((r,c))
        
        # Start BFS
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                directions = [[0,1], [0,-1], [1, 0], [-1,0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr == ROW or nc == COL or (nr,nc) in visit or grid[nr][nc] != 1):
                        continue
                    
                    grid[nr][nc] = 2
                    visit.add((nr, nc))
                    fresh -= 1
                    q.append((nr,nc))
            
            time += 1
        
        return time if fresh == 0 else -1