class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]: # means it is the same value as before
                continue

            l, r = i + 1, len(nums) - 1
            while l < r: # left and right cant be equal
                threeSum = v + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
