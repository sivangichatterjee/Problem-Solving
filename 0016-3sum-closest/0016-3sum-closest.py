class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        threesum,ans=0,0
        minsum=float("inf")
        for i in range(len(nums)):   
            l,r=i+1,len(nums)-1
            while l<r:
                threesum=nums[i]+nums[l]+nums[r]
                if target>threesum:
                    l+=1
                elif target<threesum:
                    r-=1
                else:
                    l+=1
                    r-=1
                if abs(threesum-target)<minsum:
                    minsum=abs(threesum-target)
                    ans=threesum

        return ans
        