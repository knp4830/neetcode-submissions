class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, suffix = [0] * len(height), [0] * len(height)
        total = 0


        # Calculate the Prefix for each index
        for i in range(len(height)):
            if i > 0:
                prefix[i] = max(prefix[i-1], height[i])
            else:
                prefix[i] = height[i]
        # Calculate the Suffix for each index
        for i in range(len(height) - 1, 0, -1):
            if i < len(height) - 1:
                suffix[i] = max(suffix[i+1], height[i])
            else:
                suffix[i] = height[i]

        for i in range(1, len(height) - 1):
            total += min(prefix[i], suffix[i]) - height[i]

        return total