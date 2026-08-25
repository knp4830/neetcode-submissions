class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack = []
        for i in range(len(nums)):
            if nums[i] != val:
                stack.append(nums[i])
            else:
                continue
        
        for i in range(len(nums)):
            if i < len(stack):
                nums[i] = stack[i]
            else:
                nums.pop()
        return len(nums)