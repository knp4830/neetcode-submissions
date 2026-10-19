class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Review and space optimized DP
        N, M = len(text1), len(text2)
        dp = [0] * (M + 1)

        for i in range(N):
            curRow = [0] * (M + 1)
            for j in range(M):
                if text1[i] == text2[j]:
                    curRow[j + 1] = 1 + dp[j]
                else:
                    curRow[j + 1] = max(dp[j + 1], curRow[j])
            dp = curRow

        return dp[M]