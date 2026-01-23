class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        visit=set()
        ans=[]
        def dfs(c):
            if c in visit:
                return False
            if prereq[c]==[]:
                if c not in ans:
                    ans.append(c)
                return True

            visit.add(c)
            for pre in prereq[c]:
                if not dfs(pre):
                    return False

            visit.remove(c)
            ans.append(c)
            prereq[c]=[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return ans

        