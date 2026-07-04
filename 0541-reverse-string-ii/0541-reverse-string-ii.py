class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        def reverse(start, end):
            while start<end:
                s[start],s[end]=s[end],s[start]
                start+=1
                end-=1

        for l in range(0,len(s),2*k):
            reverse(l,min(l+k-1,len(s)-1))
        
        # if len(s)<k:
        #     reverse(0,len(s)-1)
        # elif len(s)>k and len(s)<=2*k:
        #     reverse(0,k-1)
        # else:
        #     l,r=0,k-1            
        #     while l<len(s):
        #         reverse(l,r)
        #         l+=2*k
        #         r=min(l + k - 1, len(s) - 1)

        return "".join(s)



    
        