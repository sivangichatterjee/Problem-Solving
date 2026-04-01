class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countP = Counter(p)
        window = Counter()
        l = 0
        ans = []

        for r in range(len(s)):
            window[s[r]] += 1
            if r - l + 1 > len(p):
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            if window == countP:
                ans.append(l)

        return ans
        # l=0
        # ans=[]
        # while l<len(s):
        #     if ''.join(sorted(p))== ''.join(sorted(s[l:l+len(p)])):
        #         ans.append(l)
        #     l+=1

        # return ans
        # if len(s)<len(p):
        #     return []
        # l,r=0,0
        # ans=[]
        # count_S=defaultdict(int)
        # count_P=defaultdict(int)
        # for i in range(len(p)):
        #     count_S[s[i]]+=1
        #     count_P[p[i]]+=1
        
        # ans=[0] if count_S==count_P else []

        # for r in range(len(p),len(s)):
        #     count_S[s[r]]+=1
        #     count_S[s[l]]-=1
        #     if count_S[s[l]]==0:
        #         count_S.pop(s[l]) 
        #     l+=1          
        #     if count_S==count_P:
        #         ans.append(l)           

        #return ans

    #    countP=Counter(p)
    #    window=Counter()
    #    l=0
    #    ans=[]
    #    for r in range(len(s)):
    #     window[s[r]]+=1
    #     if window==countP:
    #         ans.append(l)

    #     if r-l+1>len(p):
    #         window[s[l]]-=1
    #         if window[s[l]]==0:
    #             del window[s[l]]
    #     l+=1

    #    return ans










            

        