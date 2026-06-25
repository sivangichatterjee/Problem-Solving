class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        threesum,ans=0,0
        minsum=float("inf")

        for i in range(len(nums)):

            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l,r=i+1,len(nums)-1
            while l<r:
                threesum=nums[i]+nums[l]+nums[r]
                #minsum=min(minsum, abs(threesum-target))
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
                # l+=1
                # r-=1

        return ans
        