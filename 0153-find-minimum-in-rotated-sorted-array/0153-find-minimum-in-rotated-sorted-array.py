class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,mid,right=0,0,len(nums)-1
        minimum=nums[left]
        while(left<=right):
            mid=(left+right)//2
            minimum=min(minimum,nums[mid])
            if nums[left]<nums[right]:
                minimum=min(minimum,nums[left])
                break
            else:
                if nums[mid]>=nums[left]:
                    left=mid+1                  
                else:
                    right=mid-1
        return minimum



        