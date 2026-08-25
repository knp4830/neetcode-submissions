class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Using a hashset
        # check if it is seen, if they are seen then do not return the number
        # if you iterate through the entire array and they are not seen, return that number

        seen = []

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
            else:
                seen.remove(nums[i])
        return seen[0]