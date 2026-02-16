class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        if total<abs(target):
            return 0
        if (total+target)%2!=0:
            return 0
        s=(total+target)//2
        n=len(nums)

        dp=[[0]*(s+1) for _ in range(n+1)]
        dp[0][0]=1
        # for i in range(n+1):
        #     dp[i][0]=1

        for i in range(1,n+1):
            for j in range(0, s+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[n][s]


        