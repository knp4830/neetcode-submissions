class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        minutes = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Run BFS while fresh oranges remain
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit
                        or grid[nr][nc] != 1):
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1

                    queue.append((nr, nc))
                    visit.add((nr, nc))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes