class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Math
        # you can add all the numbers [0,n]
        total = 0
        for i in range(len(nums) + 1):
            total += i
        
        for i in range(len(nums)):
            total -= nums[i]
        
        return total