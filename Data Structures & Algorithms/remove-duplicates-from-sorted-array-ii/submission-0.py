class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        L = 1

        # Go through the array
        for R in range(1, len(nums)):
            if count < 2 and nums[R] == nums[R - 1]:
                nums[L] = nums[R]
                L += 1
                count += 1
            elif nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
                count = 1

        return L           

                