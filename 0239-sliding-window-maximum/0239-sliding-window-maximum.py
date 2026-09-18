class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q=deque() #stores indices
        l=r=0
        ans=[]
        for r in range(len(nums)):
            while q and nums[r]>nums[q[-1]]:
                q.pop()

            q.append(r)

            if l>q[0]:
                q.popleft()

            if r-l+1==k:
                ans.append(nums[q[0]])
                l+=1

        return ans


        