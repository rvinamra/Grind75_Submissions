class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # initializing profit with 0
        profit = 0
        min_price = prices[0]

        if prices and len(prices) >= 2:
            
            for price in prices[1:]:
                # storing the min price to buy the stock at
                min_price = min(min_price, price) 
                # finding the max profit for the given min_price
                profit = max(profit, price - min_price)

        return profit
