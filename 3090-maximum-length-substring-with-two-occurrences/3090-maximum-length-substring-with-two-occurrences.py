class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        dist=set(s)
        count=defaultdict(int)
        r=l=maxlen=0
        for r in range(len(s)):
            count[s[r]]+=1
            while count[s[r]]>2:
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                l+=1
            #if len(count)==len(dist) :
            maxlen=max(maxlen,r-l+1)
           
        return maxlen