class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,maxlen,dup=0,0,{}
        for r in range(len(s)):
            if s[r] in dup and dup[s[r]] >=l:
                l=dup[s[r]]+1
            dup[s[r]]=r
            maxlen=max(maxlen,r-l+1)

        return maxlen
        