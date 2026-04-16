class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        fresh,time=0,0
        q=deque()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))


        while fresh and q:        
            for _ in range(len(q)):
                row, col=q.popleft()
                for dr, dc in directions:
                    nr,nc=dr+row, dc+col
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1

            time+=1

        return time if fresh==0 else -1





        
        