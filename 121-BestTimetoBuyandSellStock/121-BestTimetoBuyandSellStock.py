# Last updated: 8/23/2025, 3:27:40 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]
        profit = 0 

        for i in range(1, len(prices)):

            if (prices[i] < min_price):
                min_price = prices[i]

            profit = max(profit, prices[i] - min_price)

        return profit



        