class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Hash Set, Time and Space O(n)
        num_set = set(nums)
        n = len(nums)
        for i in range(n + 1):
            if i not in num_set:
                return i