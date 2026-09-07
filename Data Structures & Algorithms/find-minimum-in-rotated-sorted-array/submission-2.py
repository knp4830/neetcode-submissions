class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # array is sorted base case
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            # Get the minimum
            res = min(res, nums[m])
            # If the middle is less than the right we know the entire right side must be greater
            # so we search left
            if nums[m] <= nums[r]:
                r = m - 1
            # else it is greater than the right side, so we know the left side is ordered so we search
            # the right side
            else:
                l = m + 1
        
        return res