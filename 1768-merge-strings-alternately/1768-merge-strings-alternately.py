class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # l,r=0,0
        # merged=""
        # while l<len(word1) and r<len(word2):
        #     merged+=word1[l]+word2[r]
        #     l+=1
        #     r+=1
        # while l<len(word1):
        #     merged+=word1[l]
        #     l+=1
        # while r<len(word2):
        #     merged+=word2[r]
        #     r+=1

        # return merged
        i,j=0,0
        res=[]

        while i<len(word1) and j<len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)
        
        