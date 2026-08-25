class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap one pass
        prev = {}

        for i, n in enumerate(nums):
            newTarget = target - n
            if newTarget in prev:
                return [prev[newTarget], i]
            prev[n] = i