class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        top,bottom=0,m-1
        left,right=0,n-1
        while top<=bottom:
            midtop=(top+bottom)//2
            if target>matrix[midtop][right]:
                top=midtop+1
            elif target<matrix[midtop][left]:
                bottom=midtop-1
            else:
                left,right=0,n-1
                while left<=right:
                    mid=(left+right)//2
                    if target>matrix[midtop][mid]:
                        left=mid+1
                    elif target<matrix[midtop][mid]:
                        right=mid-1
                    elif target==matrix[midtop][mid]:
                        return True
                return False

        return False
        