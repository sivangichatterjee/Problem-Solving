class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        # n=len(s)
        # start=0
        # large=[]
        # for i in range(1,n+1):
        #     if i==n or s[i]!=s[i-1]:
        #         if i-start>=3:
        #             large.append([start,i-1])
        #         start=i

        # return large

        large=[]
        start=end=0
        while start<len(s):
            end=start
            while end+1<len(s) and s[start]==s[end+1]:
                end+=1
            if end-start+1>=3:
                large.append([start, end])
            start=end+1

        return large


       
            



        