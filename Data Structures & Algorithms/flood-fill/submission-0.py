class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        if start == color:
            return image
        
        m, n = len(image), len(image[0])

        def dfs(r, c):
            if (min(r, c) < 0 or r == m or c == n or image[r][c] != start):
                return
            
            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image