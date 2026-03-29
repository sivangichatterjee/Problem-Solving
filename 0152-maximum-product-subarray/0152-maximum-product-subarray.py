class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=suffix=1
        maxprod=nums[0]
        n=len(nums)
        for i in range(n):
            prefix*=nums[i]
            suffix*=nums[n-i-1]
            maxprod=max(maxprod, prefix,suffix)
            if prefix==0:
                prefix=1

            if suffix==0:
                suffix=1

            

        return maxprod


        
        