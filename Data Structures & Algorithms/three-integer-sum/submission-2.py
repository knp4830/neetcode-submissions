class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        # we use enumerate because we can pull 
        # the value already and its index
        for i, a in enumerate(nums):
            # if it isnt the first value in the input array 
            # and is the same as before we skip it
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                # We calculate the three sum total
                threeSum = a + nums[l] + nums[r]
                # If its greater than, similar to two sum 2 problem
                # We move the right pointer down
                # if its less then we move left pointer up
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                # If it does equal 0 then we append it and we increase l
                # so that we can get through the loop
                else:
                    arr.append([a, nums[l], nums[r]])
                    l += 1
                    # But! we must beware of if we increment it and its similar to last time
                    # that would make it so that we append the same solution
                    # so we check and if its the same and less than r then we increment again
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return arr