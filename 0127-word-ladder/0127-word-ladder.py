class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei=collections.defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                pattern=w[:i] + "*" + w[i+1:]
                nei[pattern].append(w)

        q=deque()
        visit=set([beginWord])
        q.append(beginWord)
        res=1

        while q:         
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pattern=word[:j] + "*" + word[j+1:]
                    for neigh in nei[pattern]:
                        if neigh not in visit:
                            q.append(neigh)
                            visit.add(neigh)

            res+=1
        return 0





        