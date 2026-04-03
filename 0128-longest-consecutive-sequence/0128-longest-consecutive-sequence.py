class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums=set(nums)
        current_streak, current_num, maxstreak=0,0,0
        for n in new_nums:
            if n-1 not in new_nums:
                current_num=n
                current_streak=1
                while current_num+1 in new_nums:
                    current_num+=1
                    current_streak+=1
                maxstreak=max(maxstreak, current_streak)

        return maxstreak
        