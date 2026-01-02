class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, count={},{}
        minlen=float("infinity")
        res=""
        if t=="": return ""

        for i in range(len(t)):
            count[t[i]]=1+count.get(t[i],0)

        need, have=len(count), 0

        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)

            if c in count and window[c]==count[c]:
                have+=1
            
            while have==need:
                if r-l+1 < minlen:
                    res=s[l:r+1]
                    minlen=r-l+1                   
                    # l+=1
                if s[l] in count and window[s[l]]==count[s[l]]:
                    have-=1
                window[s[l]]-=1
                l+=1

        return res 
        
            


        