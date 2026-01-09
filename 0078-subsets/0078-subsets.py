class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, currset=[],[]
    #     self.helper(0,nums, currset, subset)
    #     return subset

    # def helper(self, i, nums, currset, subset):
    #     if i==len(nums):
    #         subset.append(currset.copy())
    #         return
        
    #     currset.append(nums[i])
    #     self.helper(i+1, nums, currset, subset)
    #     currset.pop()

    #     self.helper(i+1, nums, currset, subset)
        def dfs(i):
            if i==len(nums):
                subset.append(currset.copy())
                return
            
            currset.append(nums[i])
            dfs(i+1)
            currset.pop()
            dfs(i+1)
        dfs(0)
        return subset

        