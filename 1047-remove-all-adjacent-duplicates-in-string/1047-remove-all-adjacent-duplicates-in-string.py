class Solution:
    def removeDuplicates(self, s: str) -> str:
        #n=len(s)
        # i=0
        # while i<len(s)-1:
        #     if s[i]==s[i+1]:
        #         s=s[:i]+s[i+2:]
        #         i=0
        #     else:
        #         i+=1
        # return s
        stack=[]
        for ch in s:
            if stack and stack[-1]==ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)