class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preMap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        order=[]

        visiting=set()
        visited=set()
        def dfs(crs):
            if crs in visiting:
                return False

            if crs in visited:
                return True

            visiting.add(crs)
            for neighbor in preMap[crs]:
                if not dfs(neighbor):
                    return False

            visiting.remove(crs)
            visited.add(crs)
            order.append(crs)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order

            

        