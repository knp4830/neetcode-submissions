class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate two points one at each end
        # we have a price counter
        # we check if the next two points price is higher than it using max
        # if it is then we will take that one and move on
        lp, rp = 0, 1
        max_profit = 0
        while rp < len(prices):
            if prices[lp] < prices[rp]:
                profit = prices[rp] - prices[lp]
                max_profit = max(max_profit, profit)
            else:
                lp = rp
            rp += 1
        return max_profit