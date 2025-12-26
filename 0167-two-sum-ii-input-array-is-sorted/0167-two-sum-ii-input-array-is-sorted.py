class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0, len(numbers)-1
        val=0
        while(left<right):
            val=numbers[left]+numbers[right]
            if val>target:
                right=right-1
            elif val<target:
                left=left+1
            else:
                return [left+1, right+1]
        