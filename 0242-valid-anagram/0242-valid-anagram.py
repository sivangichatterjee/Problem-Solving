class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1=Counter(s)
        count2=Counter(t)

        # for i in range(len(s)):
        #     count1[s[i]]+=1

        # for j in range(len(t)):
        #     count2[t[j]]+=1

        return count1==count2 
        

        