class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, curSum = 0, 0
        seen = {0 : 1}
        for n in nums:
            curSum += n
            count += seen.get(curSum - k, 0)
            seen[curSum] = seen.get(curSum, 0) + 1
        return count