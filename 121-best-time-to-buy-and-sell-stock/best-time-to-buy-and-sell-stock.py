class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, minimum = 0, prices[0]
        for i in range (1, len(prices)):
            profit = max(prices[i]-minimum, profit)
            minimum = min(minimum, prices[i])
        return profit