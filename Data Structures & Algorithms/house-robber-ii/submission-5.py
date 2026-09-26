class Solution:
    def rob(self, nums: List[int]) -> int:
        # Bottom up Neetcode Solution
        # Base case only 1
        if len(nums) == 1:
            return nums[0]
        # Otherwise we return the max between excluding house 0 and excluding last house
        return max(self.helper(nums[1:]),
                    self.helper(nums[:-1]))
        
    # Helper function skips us from repeating work
    def helper(self, nums: List[int]) -> int:
        # Base case nothing
        if not nums:
            return 0
        # Base case 1
        if len(nums) == 1:
            return nums[0]
        
        # Initialize dp and index 0 and 1
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Go through robber like usual
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        # Return the last index
        return dp[-1]