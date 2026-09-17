class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #BFS version
        start = image[sr][sc]
        # Base case
        if start == color:
            return image
        
        m, n = len(image), len(image[0]) # Get length of matrix
        q = deque([(sr, sc)]) # Start queue and initialize with starting index
        image[sr][sc] = color # Change its color
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Get directions

        # Initialze BFS
        while q:
            r, c = q.popleft() # Get row and column
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc # Helper variables
                # If it is in bound and matches the starting index change the color and add it to queue
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == start:
                    image[nr][nc] = color
                    q.append((nr, nc))
        
        return image