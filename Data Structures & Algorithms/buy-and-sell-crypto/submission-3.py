class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variable to hold profit and increment when possible
        profit = 0
        # Buy and Sell days
        left, right = 0, 1
        while right <= len(prices) - 1:
            if prices[right] >= prices[left]:
                profit = max(profit, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right = left + 1
        return profit