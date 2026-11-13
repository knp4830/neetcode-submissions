class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curEnd = farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = farthest
        return jumps