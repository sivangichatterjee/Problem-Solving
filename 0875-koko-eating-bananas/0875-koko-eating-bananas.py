class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # hours,l,r=0,1, max(piles)
        # ans=r
        # while(l<=r):
        #     m=(l+r)//2
        #     hours=0
        #     for p in piles:
        #         hours+=math.ceil(p/m)
        #     if hours<=h:
        #         ans=min(ans,m)
        #         r=m-1               
        #     else:
        #         l=m+1 
        # return ans

        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)  

            if hours > h:
                l = m + 1 
            else:
                r = m - 1 

        return l  



        