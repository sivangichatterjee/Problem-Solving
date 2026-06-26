class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        c=0
        nums.sort()
        for i in range(len(nums)-1,1,-1): # stop till 3rd element
            
            l,r=0,i-1
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    c+=r-l
                    r-=1
                else:
                    l+=1
        return c
            

        