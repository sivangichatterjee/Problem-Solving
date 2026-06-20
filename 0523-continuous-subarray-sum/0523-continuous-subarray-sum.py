class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder=defaultdict(int)
        remainder[0]=-1
        c,sum,rem=0,0,0
        for i in range(len(nums)):
            sum+=nums[i]
            rem=sum%k
            if rem not in remainder:
                remainder[rem]=i
            elif i-remainder[rem]>=2:
                return True

        return False
            
        