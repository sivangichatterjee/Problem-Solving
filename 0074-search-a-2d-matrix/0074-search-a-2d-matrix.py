class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #complexity : O(m log n)
    #     for l in matrix:
    #         if self.binary_search(l, target)==1:
    #             return True
    #     return False

    # def binary_search(self, l, target):
    #     left, right=0,len(l)-1
    #     while(left<=right):
    #         mid=(left+right)//2
    #         if target==l[mid]:
    #             return 1
    #         elif target>l[mid]:
    #             left=mid+1
    #         else:
    #             right=mid-1
    #     return -1
    #Complexity; O(log m*n)
        m,n=len(matrix),len(matrix[0])
        top, bottom=0, m-1
        while(top<=bottom):
            row=(top+bottom)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bottom=row-1
            else:
                break

        if top>bottom:
            return False
        l,r=0,n-1
        while(l<=r):
            mid=(l+r)//2
            if target>matrix[row][mid]:
                l=mid+1
            elif target<matrix[row][mid]:
                r=mid-1
            else:
                return True
        return False




            
        