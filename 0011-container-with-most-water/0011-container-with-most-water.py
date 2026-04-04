class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxArea=0
        lenght, breadth=0,0
        while l<r:
            length=min(height[l],height[r])
            breadth=r-l
            maxArea=max(maxArea, length*breadth)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return maxArea
           

        