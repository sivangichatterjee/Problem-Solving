class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            y=-heapq.heappop(stones) #max
            x=-heapq.heappop(stones) #2nd most max

            if y!=x:
                heapq.heappush(stones,-(y-x))

        return -stones[0] if stones else 0
        