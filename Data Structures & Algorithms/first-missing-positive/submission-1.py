class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Boolean array O(n) time but O(n) space
        seen = [False] * len(nums)
        for num in nums:
            if num > 0 and num <= len(nums):
                seen[num - 1] = True
        
        for num in range(1, len(nums) + 1):
            if not seen[num - 1]:
                return num
        
        return len(nums) + 1