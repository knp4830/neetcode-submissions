class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # True DP not space optimized
        N, M = len(coins), amount
        INF = float("inf")
        dp = [[INF] * (M + 1) for _ in range(N)]

        for i in range(N): 
            dp[i][0] = 0 # 0 coins make amount 0

        for c in range(1, M + 1): # Base row: only coin 0
            if c % coins[0] == 0: 
                dp[0][c] = c // coins[0] # Use 0 coins as many times as needed

        for i in range(1, N):
            for c in range(1, M + 1):
                skip = dp[i - 1][c]
                include = INF
                if c - coins[i] >= 0:
                    include = 1 + dp[i][c - coins[i]] # same row: coin i can be reused
                dp[i][c] = min(include, skip)

        return dp[N-1][M] if dp[N - 1][M] != INF else -1