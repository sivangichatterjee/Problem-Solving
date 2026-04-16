class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sr, sc=startPos
        hr,hc=homePos
        cost=0

        if sr<hr:
            for i in range(sr+1,hr+1):
                cost+=rowCosts[i]
        else:
            for i in range(sr-1,hr-1,-1):
                cost+=rowCosts[i]

        if sc<hc:
            for i in range(sc+1,hc+1):
                cost+=colCosts[i]
        else:
            for i in range(sc-1,hc-1,-1):
                cost+=colCosts[i]

        return cost

        