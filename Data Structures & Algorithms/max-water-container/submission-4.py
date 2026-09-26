class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Review
        maxWater = 0 # Keep track of maximum water
        l, r = 0, len(heights) - 1 # Left and right pointer 

        while l < r:
            # Take the max of previous or the new
            maxWater = max(maxWater, (r - l) * min(heights[l], heights[r]))

            # if right height is higher than left, we want to increment left
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return maxWater
