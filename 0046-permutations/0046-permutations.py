class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[[]]

        for n in nums:
            nextperms=[]
            for p in perms:
                for j in range(len(p)+1):
                    pcopy=p.copy()
                    pcopy.insert(j,n)
                    nextperms.append(pcopy)
            perms=nextperms
        return perms


        