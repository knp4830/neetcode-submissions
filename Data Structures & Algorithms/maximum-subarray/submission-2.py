class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Get a curSum and a maxSum
        curSum = 0
        maxSum = nums[0]

        for n in nums:
            curSum = max(curSum + n, n)
            maxSum = max(maxSum, curSum)

        return maxSum
