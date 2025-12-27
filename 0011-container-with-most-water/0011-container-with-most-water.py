class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right=0, len(height)-1
        breadth, length,max_area=0,0,0
        while(left<right):
            breadth=right-left
            length=min(height[left],height[right])
            max_area=max(max_area,breadth*length)
            if(height[left]<=height[right]):
                left=left+1
            else:
                right=right-1
        return max_area


        