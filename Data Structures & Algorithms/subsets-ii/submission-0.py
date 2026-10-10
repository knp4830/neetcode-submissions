class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset, curSet = [], []

        def helper(i):
            if i >= len(nums):
                subset.append(curSet.copy())
                return

            # Decision to Include
            curSet.append(nums[i])
            helper(i + 1)
            curSet.pop()

            # Decision to exclude (and without duplicates)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            helper(i + 1)

        helper(0)
        return subset