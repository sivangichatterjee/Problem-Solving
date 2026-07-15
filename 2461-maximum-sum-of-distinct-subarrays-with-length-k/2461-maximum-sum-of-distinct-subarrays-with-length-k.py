class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=r=0
        count=defaultdict(int)
        maxlen=sumval=0
        for r in range(len(nums)): 
            count[nums[r]]+=1
            sumval+=nums[r]
              
            if r-l+1>k:
                count[nums[l]]-=1
                sumval-=nums[l]
                if count[nums[l]]==0:
                    del count[nums[l]]
                l+=1
            if r-l+1==k and len(count)==k:
                maxlen=max(maxlen,sumval)       
            
            

        return maxlen               
                


        