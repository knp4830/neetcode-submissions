class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # Change any neg number to 0 because its not needed
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        # If value exists in input array or not
        # It has to be in bounds
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n: # In bounds
                if nums[val - 1] > 0: # if its positive we want to make negative
                    nums[val - 1] *= -1 # get the index and turn it negative to say it exists!
                elif nums[val - 1] == 0: # Edge case if it happens to be 0
                    nums[val - 1] = -1 * (len(nums) + 1) # This special value is outside of the bounds
        
        # Check if it exists
        for i in range(1, n + 1):
            if nums[i - 1] >= 0: # If its greater than 0 then we return i because it doesn't show up
                return i # We know it doesn't show up because if it does it would have been turned negative.
        
        return n + 1 # finally if it does fill the entire array we know that its the next number