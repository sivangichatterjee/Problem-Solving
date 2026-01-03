class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #o(n),o(n)-time,space
        # n=len(nums)
        # seen=set()      
        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         seen.add(nums[i])
        #     else: return nums[i]
#-----------------------------------------#
        # temp=0
        # for i in range(len(nums)):
        #     temp=nums[i]
        #     nums.remove(nums[i])
        #     if temp in nums:
        #         return temp
        #     nums.insert(i,temp)

#-----------------------------------------#

        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]

            if slow==fast:
                break

        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                break
            
        return slow



            