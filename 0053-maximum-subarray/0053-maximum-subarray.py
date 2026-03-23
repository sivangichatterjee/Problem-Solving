class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's algorithm
        maxSum=nums[0]
        curSum=0
        # for n in nums:
        #     curSum=max(curSum, 0)
        #     curSum+=n
        #     maxSum=max(curSum, maxSum)
        # return maxSum

        for n in nums:
            curSum=max(curSum+n,n)
            maxSum=max(curSum, maxSum)
        return maxSum

        #Sliding window variation
        # l,r=0,0
        # for r in range(len(nums)):
        #     if curSum<0:
        #         l=r
        #         curSum=0

        #     curSum+=nums[r]
        #     if curSum>maxSum:
        #         maxSum=curSum
        #         maxL=l
        #         maxR=r

                 
        