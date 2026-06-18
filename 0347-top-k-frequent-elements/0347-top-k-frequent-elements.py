class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #O(n log n)
        # count=Counter(nums)

        # count_sorted= sorted(count.items(), key=lambda x:x[1], reverse=True)
        # ans=[item for item,count in count_sorted[:k]]

        # return ans

        #O(n)
        freq=[[] for _ in range(len(nums)+1)]
        result=[]
        count=defaultdict(int)
        for n in nums:
            count[n]+=1
        
        for n,c in count.items():
            freq[c].append(n)

        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result


       
        

























        #  count=Counter(nums)

        # sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        # ans=[item for item, count in sorted_items[:k]]

        # return ans
                
