class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # tc O(n) and sc O(1)
        minPrice = float('inf')        
        maxProfit = 0
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = prices[i] - minPrice
            maxProfit = max(profit, maxProfit)
        
        return maxProfit