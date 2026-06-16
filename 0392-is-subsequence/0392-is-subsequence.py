class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        seq_idx=0
        for a in t:
            if seq_idx==len(s):
                break
            if a==s[seq_idx]:
                seq_idx+=1

        return seq_idx==len(s)

        