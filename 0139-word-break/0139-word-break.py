class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
         worddict=set(wordDict)
         words=[-1]
         for i in range(len(s)):
            for w in words:
                if s[w+1:i+1] in worddict:
                    words.append(i)
                    break

         return len(s)-1 in words
        