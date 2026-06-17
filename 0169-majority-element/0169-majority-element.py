class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #solution1 
        # count=defaultdict(int)
        # res, maxcount=0,0
        # for n in nums:
        #     count[n]+=1
        #     res=n if count[n]>maxcount else res
        #     maxcount=max(count[n],maxcount)
        # return res

        # for k,v in count.items():
        #     if v>(len(nums)//2):
        #         return k

        #solution2
        # Boyer-Moore 
        # count, res=0,0
        # for n in nums:
        #     if count==0:
        #         res=n
        #     if res==n:
        #         count+=1
        #     else:
        #         count-=1

        # return res

        return sorted(nums)[len(nums)//2]

        
        