class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for l in range(n - 1, -1 ,-1):          # l goes backward
            dp[l][l] = 1                        # single char
            for r in range(l + 1, n):           # r goes forward
                if s[l] == s[r]:
                    dp[l][r] = 2 + dp[l + 1][r - 1]         # keep both ends
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])  # drop left or drop right
        
        return dp[0][n - 1]