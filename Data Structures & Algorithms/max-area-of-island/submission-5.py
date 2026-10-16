class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Review BFS with Visit
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(grid), len(grid[0])
        area = 0
        visit = set()
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            res = 1

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (min(nr,nc) < 0 or nr == rows or nc == cols or 
                        (nr,nc) in visit or grid[nr][nc] == 0):
                        continue

                    q.append((nr,nc))
                    visit.add((nr,nc))
                    res += 1
            return res

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == 1:
                    area = max(area, bfs(r,c))

        return area