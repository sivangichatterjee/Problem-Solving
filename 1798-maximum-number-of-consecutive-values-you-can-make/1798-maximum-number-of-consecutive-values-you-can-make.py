class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        change,ct=0,0
        for coin in coins:
            if coin>change+1:
                return change+1
            change+=coin
            #ct+=1
        return change+1



        