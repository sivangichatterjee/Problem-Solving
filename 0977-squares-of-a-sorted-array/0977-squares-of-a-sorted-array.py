class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r=0,0
        res=[]
        while r<len(nums) and nums[r]<0:
            r+=1
        l=r-1
        while l>=0 or r<len(nums):
            if r >= len(nums) or (l>=0 and abs(nums[l])<abs(nums[r])):
                res.append(nums[l]*nums[l])
                l-=1
            else:
                res.append(nums[r]*nums[r])
                r+=1

        return res

        # n=len(nums)
        # l,r=0,n-1
        # res=[0]*len(nums)
        # i=0
        # while l<=r:
        #     if abs(nums[l])<abs(nums[r]):
        #         res[n-1-i]=nums[r]*nums[r]
        #         r-=1
        #     else:
        #         res[n-1-i]=nums[l]*nums[l]
        #         l+=1
        #     i+=1

        # return res
            
            

        