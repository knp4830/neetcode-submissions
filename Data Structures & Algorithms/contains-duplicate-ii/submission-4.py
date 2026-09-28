class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Initialize our window set
        window = set()
        L = 0 # Left pointer

        # One loop where R is the right pointer
        for R in range(len(nums)):
            if (R - L) > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False