class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Review BFS
        start = image[sr][sc]
        if start == color:
            return image

        rows, cols = len(image), len(image[0])
        queue = deque([(sr,sc)]) # Queue the start
        image[sr][sc] = color # mark the start as soon as its enqueued

        while queue:
            r, c = queue.popleft()
            for dr, dc in [[0,1], [0, -1], [1,0], [-1,0]]:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0 or nr == rows or nc == cols or image[nr][nc] != start):
                    continue
                image[nr][nc] = color
                queue.append((nr,nc))

        return image