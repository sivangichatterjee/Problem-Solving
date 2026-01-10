class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, currset=[],[]
        n=len(candidates)
        def backtrack(i):
            if sum(currset)==target:
                res.append(currset.copy())
                return
            elif sum(currset)>target:
                return

            for j in range(i,n):
                currset.append(candidates[j])
                backtrack(j)
                currset.pop()

        backtrack(0)
        return res

        