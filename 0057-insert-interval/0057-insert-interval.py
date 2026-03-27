class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        i=0
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval[0]=min(newInterval[0],intervals[i][0])
                newInterval[1]=max(newInterval[1],intervals[i][1])
            
        res.append(newInterval)
        return res
        # n=len(intervals)
        # i=0
        # while i<n and intervals[i][1]<newInterval[0]:
        #     res.append(intervals[i])
        #     i+=1

        # while i<n and intervals[i][0]<=newInterval[1]:
        #     newInterval[0]=min(intervals[i][0],newInterval[0])
        #     newInterval[1]=max(intervals[i][1],newInterval[1])
        #     i+=1
        # res.append(newInterval)
        # return res+intervals[i:]

        # while i<n:
        #     res.append(intervals[i])
        #     i+=1

        #return res

        

        
        