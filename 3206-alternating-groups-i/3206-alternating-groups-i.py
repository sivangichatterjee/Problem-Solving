class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
       n=len(colors)
       c=0
       for i in range(n):
            left=colors[i-1]
            middle=colors[i]
            right=colors[(i+1)%n]

            if middle!=left and middle!=right:
                c+=1
       return c




        