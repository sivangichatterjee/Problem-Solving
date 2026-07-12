class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        minsum=float("inf")
        total=0
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                minsum=min(minsum, r-l+1)
                total-=nums[l]
                l+=1

        return minsum if minsum!=float("inf") else 0
        