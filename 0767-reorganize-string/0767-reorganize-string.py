class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        res=""
        # count=defaultdict(int)
        # for i in range(len(s)):
        #     count[s[i]]+=1

        maxHeap=[[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        prev=None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char= heapq.heappop(maxHeap) 
            res+=char   
            cnt+=1 #since cnt is negative and we are decreasing value 

            if prev:
                heapq.heappush(maxHeap, prev)
                prev=None
            
            if cnt!=0:
                prev=[cnt,char]

        return res
