class Solution:
    def trap(self, height: List[int]) -> int:
        # Review
        # Two Pointers and we keep track of the max height at current iterations
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        # Total water tracker
        res = 0
        while l < r:
            # If the height of the left is smaller than the height of the right it means we can
            # keep water in on the left
            if height[l] < height[r]:
                # Thus we increase left
                l += 1
                # And we check if the left before it was higher or not
                leftMax = max(leftMax, height[l])
                # If it was higher we add that to the result, and if it wasn't then we will get a 0 anyways
                res += leftMax - height[l]
            else:
                # Same for right side
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res
            