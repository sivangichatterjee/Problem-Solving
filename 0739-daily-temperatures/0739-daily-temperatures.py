class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Complexity - O(n^2)
        # stack,ans=[],[]
        # n=len(temperatures)
        # for i in range(n):
        #     c=1
        #     j=i+1
        #     while j<n:
        #         if temperatures[j]>temperatures[i]:
        #             break
        #         j=j+1
        #         c=c+1
        #     c=0 if j==n else c
        #     ans.append(c)
        # return ans

        #Complexity - O(n)
        stack=[] # stack [temperature, index]
        ans=[0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT, stackInd=stack.pop()
                ans[stackInd]=i-stackInd
            stack.append((t,i))
        return ans
            
            

        