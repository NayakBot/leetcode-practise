class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        n = len(prices)
        maxProfit = 0

        while sell < n:
            profit = prices[sell] - prices[buy]

            if prices[sell] > prices[buy]:
                maxProfit = max(maxProfit, profit)
            else:
                buy = sell
            
            sell += 1

        return maxProfit