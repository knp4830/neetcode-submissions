class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap
        H = {} 
        for i, n in enumerate(nums):
            H[n] = i
        for i in range(len(nums)):
            newTarget = target - nums[i]
            if newTarget in H and H[newTarget] != i:
                arr = [i, H.get(newTarget)]
                return arr