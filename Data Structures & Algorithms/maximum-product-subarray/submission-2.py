class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Because we are looking contiguous subarray and O(n) time and O(1) space
        # We can iterate through the array and store at the current index the product, made from the las
        # so [2,4,-3,5] would be something like [2,8,-3,5]

        curMax = curMin = res = nums[0]
        for i in range(1, len(nums)):
            candidates = (nums[i], curMax * nums[i], curMin * nums[i])
            curMax = max(candidates)
            curMin = min(candidates)
            res = max(res, curMax)
        
        return res
