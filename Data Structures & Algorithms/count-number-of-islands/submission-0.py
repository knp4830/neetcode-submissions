class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: # base case, there is no grid
            return 0

        def bfs(r, c):

            search_q = deque()
            visit.add((r, c)) #use a set cause it does not allow for duplicates
            search_q.append((r,c))

            while search_q:

                row, col = search_q.popleft()
                directions = [[1, 0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r, c = row+dr, col+dc

                    if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r,c) not in visit):

                        search_q.append((r,c))
                        visit.add((r,c))

        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set() # keeps track of all the elements in the matrix that we visited or not.

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    count += 1

        return count