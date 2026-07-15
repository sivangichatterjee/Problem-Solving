class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=r=c=maxlen=0
        count=defaultdict(int)
        for r in range(len(nums)):
            count[nums[r]]+=1
            if nums[r]==1:
                c+=1
            if r-l+1-c>k:
                count[nums[l]]-=1
                if nums[l]==1:
                    c-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen
        