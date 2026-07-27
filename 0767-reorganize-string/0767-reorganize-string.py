class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        #no char may exceed (n+1)//2
        if max(count.values())>(len(s)+1)//2:
            return ""
        maxHeap=[[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev=None
        res=[]

        while maxHeap:
            cnt,char=heapq.heappop(maxHeap)
            res.append(char)
            if prev and prev[0]<0:  # since maxheap values are negative, it needs to be <0
                heapq.heappush(maxHeap, prev)
            prev=[cnt+1,char]

        return "".join(res)
        