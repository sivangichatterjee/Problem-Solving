class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minlen=float("inf")
        l=r=0
        count=defaultdict(int)
        for r in range(len(cards)):           
            if cards[r] in count:
                minlen=min(minlen, r-count[cards[r]]+1)
            count[cards[r]]=r

        return minlen if minlen!=float("inf") else -1


        