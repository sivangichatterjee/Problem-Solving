class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen=0
        count=defaultdict(int)
        l,r=0,0
        for r in range(len(s)):
            count[s[r]]+=1
            if r-l+1 - max(count.values())>k:
                count[s[l]]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)

        return maxlen



        