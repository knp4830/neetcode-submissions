class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Base case
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True                                     # Empty + Empty = Empty

        for i in range(m + 1):
            for j in range(n +1):
                k = i + j - 1                                   # Index of the s3 character this cell adds
                if i > 0 and dp[i - 1][j] and s1[i - 1] == s3[k]:
                    dp[i][j] = True                             # Came from above, used s1
                if j > 0 and dp[i][j - 1] and s2[j - 1] == s3[k]:
                    dp[i][j] = True                             # Came from left, used s2
        
        return dp[m][n]