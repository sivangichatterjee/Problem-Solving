class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)

        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        ans=[item for item, count in sorted_items[:k]]

        return ans
                

        