class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel = set(days) # O(1) - Is this a travel day
        dp = [0] * (days[-1] + 1) # dp[d] = min cost to cover all travel days

        for d in range(1, days[-1] + 1):
            if d not in travel:
                dp[d] = dp[d - 1] # Nothing to cover today: same cost as yesterday
                continue

            dp[d] = min(dp[d - 1] + costs[0],           # 1 - day pass covering today
                        dp[max(0, d - 7)] + costs[1],   # 7 - day pass covering days d-6..d
                        dp[max(0, d - 30)] + costs[2])  # 30 - day pass covering days d-29..d

        
        return dp[days[-1]]
