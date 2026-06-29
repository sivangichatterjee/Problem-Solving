class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r=0,len(people)-1
        ct=0
        while l<=r:
            if l!=r and people[l]+people[r]<=limit:
                l+=1
                r-=1
                ct+=1
            else:
                r-=1
                ct+=1
        return ct
        # for i, r in enumerate(people):
        #     sum+=r
        #     if sum==limit:
        #         sum=0
        #         ct+=1
        #     elif sum>limit:
        #         ct+=1
        #         sum=r           


        # return ct


        