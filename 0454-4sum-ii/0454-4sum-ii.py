class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count=defaultdict(int)
        n=len(nums1)
        res,sum1,sum2=0,0,0

        for i in range(n):
            for j in range(n):
                sum1=nums1[i]+nums2[j]
                count[sum1]+=1
        for i in range(n):
            for j in range(n):
                sum2=nums3[i]+nums4[j]
                if -sum2 in count:
                    res+=count[-sum2]

        return res



        