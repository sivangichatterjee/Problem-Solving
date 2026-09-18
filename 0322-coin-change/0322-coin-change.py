class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n=len(coins)
        INF=10**9
        dp=[[INF]*(amount+1) for _ in range(n+1)] # col->amount, row->number of coins

        for i in range(n+1):
            dp[i][0]=0 #first column=0

        dp[0][0]=INF
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(dp[i-1][j], 1+dp[i][j-coins[i-1]]) #minimum of exlusion and inclusion
                    #1+dp[i][j-coins[i-1]] because unbounded and can include the same coin as many times, and j-coins[i-1] to account fo rthe value we are including
                else:
                    dp[i][j]=dp[i-1][j] # if value is more, we will have to exclude it 

        return -1 if dp[n][amount]==INF else dp[n][amount]

        