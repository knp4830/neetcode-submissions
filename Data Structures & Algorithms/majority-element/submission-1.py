class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        curNum = nums[0]
        for n in range(1, len(nums)):
            if count == 0:
                curNum = nums[n]
                count += 1
            elif nums[n] != curNum and count != 0:
                count -= 1
            else:
                count += 1
        
        return curNum