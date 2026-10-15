class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        minutes = 0
        # Check for all rotten fruit and add it to the queue first
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c)) # If it is rotten, add it to the queue
                    visit.add((r,c)) # Make sure to mark it as visited

        # Run BFS
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                neighbors = [[0,1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    # Out of bounds, is already rotten or isn't a fruit (0)
                    if (min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols 
                        or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 0):
                        continue
    
                    grid[r + dr][c + dc] = 2
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            minutes += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return max(0, minutes - 1)