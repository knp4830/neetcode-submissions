class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # DFS approach
        memo = {}

        def dfs(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if (l, r) in memo:
                return memo[(l, r)]
            
            if s[l] == s[r]:
                res = 2 + dfs(l + 1, r - 1)
            else:
                res = max(dfs(l + 1, r), dfs(l, r - 1)) # drop left or drop right
            
            memo[(l, r)] = res
            return res

        return dfs(0, len(s) - 1)


        