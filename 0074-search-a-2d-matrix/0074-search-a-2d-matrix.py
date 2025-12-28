class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for l in matrix:
            if self.binary_search(l, target)==1:
                return True
        return False

    def binary_search(self, l, target):
        left, right=0,len(l)-1
        while(left<=right):
            mid=(left+right)//2
            if target==l[mid]:
                return 1
            elif target>l[mid]:
                left=mid+1
            else:
                right=mid-1
        return -1


            
        