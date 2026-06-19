class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        count1,count2,res1,res2=0,0,None, None
        for n in nums:
            if n==res1:
                count1+=1
            elif n==res2:
                count2+=1
            elif count1==0:
                res1,count1=n,1
            elif count2==0:
                res2,count2=n,1
            else:
                count1-=1
                count2-=1

        if res1 is not None and nums.count(res1)>len(nums)//3:
            ans.append(res1) 
        if res2 is not None and nums.count(res2)> len(nums)//3:
            ans.append(res2)

        return ans


        