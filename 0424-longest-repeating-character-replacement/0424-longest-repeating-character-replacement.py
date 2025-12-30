class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen,l,r, dup=0,0,0,defaultdict(dict)
        for r in range(len(s)):
            dup[s[r]]=1+dup.get(s[r],0)
            if r-l+1 - max(dup.values())>k:
                dup[s[l]]-=1
                l+=1
            maxLen=max(maxLen, r-l+1)
        return maxLen
            
