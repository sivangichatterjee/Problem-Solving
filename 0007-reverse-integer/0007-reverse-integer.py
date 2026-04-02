class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1   # 2147483647
        INT_MIN = -2**31      # -2147483648

        copy=x
        rev=0
        
        x=abs(x)

        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10

        if rev> INT_MAX or rev< INT_MIN:
            return 0

        return -(rev) if copy<0 else rev




        