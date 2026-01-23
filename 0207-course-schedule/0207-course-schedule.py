class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        visit=set()
        def dfs(c):
            if c in visit:
                return False
            if prereq[c]==[]:
                return True
            visit.add(c)
            for pre in prereq[c]:
                if not dfs(pre): 
                    return False
            visit.remove(c)
            prereq[c]=[]
            return True


        for c in range(numCourses):
            if not dfs(c): return False

        return True

        