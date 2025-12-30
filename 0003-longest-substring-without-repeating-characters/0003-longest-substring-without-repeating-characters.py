class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,maxLen,dup=0,0,{}
        for r in range(len(s)):
            if s[r] in dup and dup.get(s[r])>=l :
                l=dup.get(s[r])+1
            dup[s[r]] = r
            maxLen=max(maxLen,r-l+1)
        return maxLen
        