class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l=r=best=0
        window=0
        baseline=sum(customers[c] for c in range(len(customers)) if grumpy[c]==0)
        for r in range(len(customers)):
            if grumpy[r]==1:
                window+=customers[r]
            if r-l+1>minutes:
                if grumpy[l]==1:
                    window-=customers[l]
                l+=1
            best=max(best, window)

        return baseline+best



        