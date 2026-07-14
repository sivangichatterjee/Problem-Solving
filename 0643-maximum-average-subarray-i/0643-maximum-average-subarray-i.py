class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=r=0
        maxavg=float("-inf")
        sum=avg=0
        for r in range(len(nums)):
            sum+=nums[r]
            if r-l+1>k:
                sum-=nums[l]
                l+=1
            if r-l+1==k:
                avg=sum/k               
                maxavg=max(avg,maxavg)

        return maxavg
        