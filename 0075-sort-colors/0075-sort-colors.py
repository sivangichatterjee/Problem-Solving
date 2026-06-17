class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zeros,ones,twos=0,0,0
        # for n in nums:
        #     if n==0:
        #         zeros+=1
        #     elif n==1:
        #         ones+=1
        #     else:
        #         twos+=1

        # nums[:zeros]=[0]*zeros
        # nums[zeros:(zeros+ones)]=[1]*ones
        # nums[(zeros+ones):len(nums)]=[2]*twos

        #part 2
        count=[0]*3
        for num in nums:
            count[num]+=1
        
        index=0
        for i in range(3):
            while count[i]:
                nums[index]=i
                count[i]-=1               
                index+=1


        #dutch national flag algorithm
        # low,mid,high=0,0,len(nums)-1
        
        # while(mid<=high):
        #     if nums[mid]==0:
        #         nums[mid], nums[low]=nums[low],nums[mid]
        #         low+=1
        #         mid+=1
        #     elif nums[mid]==1: 
        #         mid+=1
        #     else:
        #         nums[mid], nums[high]=nums[high],nums[mid]
        #         high-=1
                



        