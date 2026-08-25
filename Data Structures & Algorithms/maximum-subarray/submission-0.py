class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i, n in enumerate(nums):
            dp[i] = max(n, dp[i-1] + n)

        return max(dp)