class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1count,s2count=defaultdict(int),defaultdict(int)
        matches=0

        for i in range(len(s1)):
            s1count[s1[i]]+=1
            s2count[s2[i]]+=1

        l=0
        keys=set(s1count)|set(s2count)
        matches=sum(1 for c in s1count if s1count[c]==s2count[c])
        for r in range(len(s1),len(s2)):
            if matches==len(s1count):
                return True

            c=s2[r]
            s2count[c]+=1
            if c in s1count:
                if s1count[c]==s2count[c]:
                    matches+=1
                elif s1count[c]+1==s2count[c]:
                    matches-=1

            c=s2[l]
            s2count[c]-=1
            if c in s1count:
                if s1count[c]==s2count[c]:
                    matches+=1
                elif s1count[c]-1==s2count[c]:
                    matches-=1

            l+=1

        return matches==len(s1count)
        