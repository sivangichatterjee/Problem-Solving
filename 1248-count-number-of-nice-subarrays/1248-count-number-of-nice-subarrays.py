class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        count[0]=1
        rem,c,odd=0,0,0
        for n in nums:
            if n%2!=0:
                odd+=1
            rem=odd-k
            if rem in count:
                c+=count[rem]
            count[odd]+=1
        return c
        