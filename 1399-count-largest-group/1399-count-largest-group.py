class Solution:
    def countLargestGroup(self, n: int) -> int:
        ans=defaultdict(int)
        if n<10:
            return n
        for i in range(1, n+1):
            if i>=10:
                ans[self.sum(i)]+=1
            else:
                ans[i]+=1

        max_freq=max(ans.values())

        count =sum(1 for v in ans.values() if v==max_freq)

        return count
   
    def sum(self, n):
        sum=0
        while n>0:
            sum+=n%10
            n=n//10
        return sum