class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=r=maxlen=c=0
        count=defaultdict(int)
        for r in range(len(nums)):
            count[nums[r]]+=1
            if nums[r]==1:
                c+=1
            if r-l+1 - c>1:
                count[nums[l]]-=1
                if nums[l]==1:
                    c-=1
                l+=1 
            if r-l+1-c<=1:          
                maxlen=max(c,maxlen)

        return maxlen if c!=len(nums) else maxlen-1

        