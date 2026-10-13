class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # O(n * m) Time and Space
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1 # 1 way to sum to zero with 0 elements

        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i + 1][cur_sum + nums[i]] += count
                dp[i + 1][cur_sum - nums[i]] += count

        return dp[len(nums)][target]