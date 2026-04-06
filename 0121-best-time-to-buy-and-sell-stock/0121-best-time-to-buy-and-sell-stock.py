class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=prices[0]
        profit,maxProfit=0,0
        for i in range(1,len(prices)):
            profit=prices[i]-minimum
            maxProfit=max(maxProfit,profit)
            minimum=min(prices[i],minimum)

        return maxProfit


        

        