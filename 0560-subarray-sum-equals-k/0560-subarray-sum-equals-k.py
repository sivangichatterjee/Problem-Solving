class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        count[0]=1
        c=sum=rem=0
        for n in nums:
            sum+=n
            rem=sum-k
            if rem in count:
                c+=count[rem]
            count[sum]+=1

        return c