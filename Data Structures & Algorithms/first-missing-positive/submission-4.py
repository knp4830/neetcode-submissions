class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Review of Optimal Solution
        n = len(nums)

        # Negative numbers are changed to 0
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        # Mark each value val in 1..n, make it negative
        # Values outside 1..n are ignored: they have no matching index
        # values outside 1..n can't affect the answer
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1

        # Special Case, if its 0, we make it negative and outside the bounds so it won't affect us
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        # Now we check if the index is present by seeing if it is less than 0
        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                return i

        return n + 1