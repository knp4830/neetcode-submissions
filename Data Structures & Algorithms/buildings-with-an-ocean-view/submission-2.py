class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        w = n # next write position (moves left)
        tallest = 0

        for i in range(n - 1, - 1, -1):
            if heights[i] > tallest:
                tallest = heights[i]
                w -= 1
                heights[w] = i

        return heights[w:]