class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=maxlen=zeros=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            if zeros>1:
                if nums[l]==0:
                    zeros-=1
                l+=1
            maxlen=max(r-l+1-1, maxlen)
        return maxlen

        