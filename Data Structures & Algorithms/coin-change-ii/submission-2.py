class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DP non space optimized
        N, M = len(coins), amount
        dp = [[0] * (M + 1) for _ in range(N + 1)] # row 0 = no coins used yet

        for i in range(N + 1):
            dp[i][0] = 1                # Always 1 way to  make amount 0: take nothing

        for i in range(1, N + 1):
            coin = coins[i - 1]         # row i uses coins[i - 1] (row offset)
            for a in range(1, M + 1):
                skip = dp[i - 1][a]     # Ways without this coin (above)
                include = 0
                if a - coin >= 0:
                    include = dp[i][a - coin] # Ways using this coin again
                dp[i][a] = skip + include
        
        return dp[N][M]