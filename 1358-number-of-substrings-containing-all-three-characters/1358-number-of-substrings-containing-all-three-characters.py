class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=defaultdict(int)
        l=r=ct=0
        while r<len(s):
            count[s[r]]+=1
            while len(count)==3:
                ct+=len(s)-r               
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                l+=1

            r+=1

        return ct



        