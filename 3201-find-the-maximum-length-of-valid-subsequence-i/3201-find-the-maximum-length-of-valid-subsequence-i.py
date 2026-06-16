class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_count=0
        odd_count=0
        for num in nums:
            if num%2==0:
                even_count+=1
            else:
                odd_count+=1

        alt_count=0
        prev=None
        for num in nums:
            curr=num%2
            if prev!=curr:
                alt_count+=1
                prev=curr

        return max(even_count,odd_count,alt_count)


        