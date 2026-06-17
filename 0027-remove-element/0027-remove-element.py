class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ct,low=0,0
        for i in range(len(nums)):
            if nums[i]!=val:
                ct+=1
                nums[low],nums[i]=nums[i],nums[low]
                low+=1

        return ct
        