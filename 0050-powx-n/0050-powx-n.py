class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==0:
            return 1
        
        N=abs(n)
        res=1
        while N>0:
            if N%2==1:
                res*=x
            x*=x
            N=N//2

        return res if n>0 else 1/res
        
            

        