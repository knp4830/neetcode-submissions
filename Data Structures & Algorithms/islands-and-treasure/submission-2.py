class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Same solution with a slight change in syntax
        rows, cols = len(grid), len(grid[0])
        visit = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                 if grid[r][c] == 0:
                    visit.add((r,c))
                    queue.append((r,c))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                neighbors = [[0,1], [0,-1], [1, 0], [-1, 0]]

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (min(nr,nc) < 0 or nr == rows or nc == cols or (nr,nc) in visit
                        or grid[nr][nc] == -1):
                        continue
                    
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))
                    visit.add((nr,nc))

        


