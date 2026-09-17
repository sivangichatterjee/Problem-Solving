class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq=[[] for _ in range(len(nums)+1)]
        count=Counter(nums)
        for n, c in count.items():
            freq[c].append(n)

        result=[]

        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result

        

        