class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, currset=[],[]

        def backtrack(i):
            if len(currset)==k:
                res.append(currset.copy())
                return
            if i>n:
                return
            
            # currset.append(i)
            # backtrack(i+1)
            # currset.pop()
            # backtrack(i+1)
            for j in range(i, n+1):
                currset.append(j)
                backtrack(j+1)
                currset.pop()

        backtrack(1)
        return res
        