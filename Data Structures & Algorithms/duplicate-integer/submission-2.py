class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Making a set removes repeated numbers
        seen = set()
        for i in range(len(nums)):
            seen.add(nums[i])
        # If the num in set is not equal to the num in nums we return false
        if len(seen) < len(nums):
            return True
        else:
            return False