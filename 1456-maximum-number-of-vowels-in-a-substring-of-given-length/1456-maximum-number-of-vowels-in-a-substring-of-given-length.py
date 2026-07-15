class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=r=count=maxlen=0
        vowels=set('aeiou')
        for r in range(len(s)):
            if s[r] in vowels:
                count+=1
            if r-l+1>k:
                if s[l] in vowels:
                    count-=1
                l+=1
            if r-l+1==k:
                maxlen=max(maxlen,count)

        return maxlen

        