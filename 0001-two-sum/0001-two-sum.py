class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        ans={}
        while i<len(nums):
            left=target-nums[i]
            if left in ans:
                return [ans[left],i]
            else:
                ans[nums[i]]=i
            i+=1


        