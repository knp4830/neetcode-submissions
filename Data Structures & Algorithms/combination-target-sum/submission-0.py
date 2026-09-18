class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(i, cur, total):
            # Base case success
            if total == target:
                res.append(cur.copy())
                return
            # i is out of bounds
            if i >= len(nums) or total > target:
                return

            # First decision to include the candidate
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # Decision to not include the candidate
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
            
