class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count=defaultdict(int)
        count[0]=-1
        long,total=0,0
        for i in range(len(nums)):
            if nums[i]==1:
                total+=1
            else:
                total-=1
            if total in count:
                long=max(long, i-count[total])
            else:
                count[total]=i

        return long
            
        