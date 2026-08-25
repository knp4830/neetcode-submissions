class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # are there two numbers that equal each other? yes?
        # is their absolute value distance less than or equal to k? return true
        # if not return false.
        # because we want the length to be <= k, we take index r - l and compare to k

        l = 0
        r = 1

        while r < len(nums):
            if nums[l] != nums[r]:
                r += 1
            elif nums[l] == nums[r] and r - l <= k:
                return True
            else:
                l = r 
                r += 1


        return False