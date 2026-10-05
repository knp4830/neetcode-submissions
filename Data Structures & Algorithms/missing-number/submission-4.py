class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sorting
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return i + 1