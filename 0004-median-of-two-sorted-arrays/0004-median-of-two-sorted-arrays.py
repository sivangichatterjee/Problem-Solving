class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1.extend(nums2)
        # nums1.sort()
        # n=len(nums1)
        # if n%2==0:
        #     return ((nums1[n//2]+nums1[(n//2)-1])/2)
        # else:
        #     return nums1[n//2]

        total=len(nums1)+len(nums2)
        half=total//2
        if len(nums1)<len(nums2):
            A,B=nums1,nums2
        else:
            B,A=nums1, nums2

        l,r=0,len(A)-1
        while True:
            m=(l+r)//2 # middle index for A
            n=half-m-2 # B ->since indices start from 0 
            Aleft=A[m] if m>=0 else float("-infinity")
            Aright=A[m+1] if m+1<len(A) else float("infinity")
            Bleft=B[n] if n>=0 else float("-infinity")
            Bright=B[n+1] if n+1<len(B) else float("infinity")

            if Aleft<=Bright and Aright>=Bleft:
                if total%2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=m-1
            else:
                l=m+1


        