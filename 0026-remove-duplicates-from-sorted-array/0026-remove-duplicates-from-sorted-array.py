class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # i,j=0,0
        # while i<len(nums)-1:
        #     if nums[i]==nums[i+1]:
        #         nums.pop(i)
        #     else:
        #         i+=1

        # return len(nums)

        l=1
        r=1

        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1

        return l

        