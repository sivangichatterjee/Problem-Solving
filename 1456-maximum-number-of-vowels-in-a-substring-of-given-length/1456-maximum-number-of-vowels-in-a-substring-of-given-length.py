class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=r=0
        count=0
        maxlen=c=0
        vowels=set('aeiou')
        for r in range(len(s)):
            if s[r] in vowels:
                count+=1            
            if r-l+1>k:
                if s[l] in vowels:
                    count-=1
                l+=1
            if r-l+1==k:
                maxlen=max(count,maxlen)

        return maxlen

        #     count[s[r]]+=1
        #     if r-l+1>k:
        #         count[s[l]]-=1
        #         l+=1
        #     if s[r] in 'aeiou':
        #         count[s[r]]+=1
        #         l=r
        #     if r-l+1==k:
        #         c=sum(count.values())
        #     maxlen=max(maxlen,c)

        # return maxlen