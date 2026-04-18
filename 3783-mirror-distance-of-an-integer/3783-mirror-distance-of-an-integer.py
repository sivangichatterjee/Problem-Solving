class Solution:
    def mirrorDistance(self, n: int) -> int:
        copy=n
        rev,rem=0,0
        while n>0:
            rem=n%10
            rev=rev*10+rem
            n=n//10
        return abs(rev-copy)
        