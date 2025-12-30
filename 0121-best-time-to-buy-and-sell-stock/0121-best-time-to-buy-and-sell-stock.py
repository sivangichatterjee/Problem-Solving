class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, maxProfit=prices[0], 0
        for i in range(len(prices)):
            profit=prices[i]-minimum
            maxProfit=max(maxProfit, profit)
            minimum=min(minimum, prices[i])
        return maxProfit

        