class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Math optimal
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]

        return res