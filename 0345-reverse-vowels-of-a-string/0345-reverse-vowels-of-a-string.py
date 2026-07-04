class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        def is_vowel(c):
            return c in 'aeiouAEIOU'

        l,r=0,len(s)-1
        while l<r:
            while l<r and not is_vowel(s[l]):
                l+=1
            while l<r and not is_vowel(s[r]):
                r-=1
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1

        return ''.join(s)

        