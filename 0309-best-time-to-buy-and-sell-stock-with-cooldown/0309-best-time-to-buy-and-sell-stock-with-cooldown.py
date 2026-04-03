class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}

        def dfs(i,buying):
            if i>=len(prices):
                return 0

            if (i,buying) in dp:
                return dp[(i,buying)]

            if buying:
                buy=dfs(i+1,buying=False)-prices[i]
                cooldown=dfs(i+1,buying=True)
                dp[(i,buying)]=max(buy,cooldown)

            else:
                sell=dfs(i+2,buying=True)+prices[i]
                cooldown=dfs(i+1,buying=False)
                dp[(i,buying)]=max(sell,cooldown)
            return dp[(i,buying)]

        return dfs(0,True)
            





        