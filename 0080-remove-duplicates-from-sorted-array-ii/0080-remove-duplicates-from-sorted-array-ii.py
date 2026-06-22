class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=2
        for r in range(2, len(nums)):
            if nums[r]!=nums[l-2]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1

        return l

        