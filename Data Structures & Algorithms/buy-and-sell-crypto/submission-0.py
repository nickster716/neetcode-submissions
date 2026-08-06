class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        minBuyPrice = [minPrice] * len(prices)

        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            minBuyPrice[i] = minPrice
        
        maxProfit = 0
        for i in range(len(prices)):
            profit = prices[i] - minBuyPrice[i]
            maxProfit = max(profit, maxProfit)
        
        return maxProfit
