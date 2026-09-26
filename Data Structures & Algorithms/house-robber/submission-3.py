class Solution:
    def rob(self, nums: List[int]) -> int:
        # Bottom up, initialize an array the size of nums
        # Get length of nums just to make it easy
        n = len(nums)
        
        # Base case 1 house
        if n == 1:
            return nums[0]
        
        # Initialize dp array
        dp = [0] * n
        
        # Base numbers, 0 is always 0
        dp[0] = nums[0]
        # dp at 1 is the best of either houses
        dp[1] = max(nums[0], nums[1])

        # Starting from range 2 to the end, we either take the previous or the current plus the house 2 before.
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        # Return the end of the array 
        return dp[-1]

        