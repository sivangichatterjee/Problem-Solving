class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count=defaultdict(int)
        maxlen=ct=l=r=0
        for r in range(len(fruits)):
            count[fruits[r]]+=1           
            if len(count)>2:
                count[fruits[l]]-=1
                if count[fruits[l]]==0:
                    del count[fruits[l]]
                l+=1
            if len(count)<=2:
                ct=r-l+1
                maxlen=max(maxlen,ct)
            

        return maxlen
        