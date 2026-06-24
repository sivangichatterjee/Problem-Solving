class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l=0
        for r in range(1,len(nums),2):
            if nums[r]%2==0:
                while nums[l]%2==0:
                    l+=2
                nums[l], nums[r] = nums[r], nums[l]
            
        return nums
        