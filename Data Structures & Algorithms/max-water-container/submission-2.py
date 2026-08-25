class Solution:
    def maxArea(self, heights: List[int]) -> int:

        area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            length = r - l
            maxHeight = min(heights[l], heights[r])
            area = max(area, length * maxHeight)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return area

