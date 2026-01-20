class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit=set()
        rows, cols=len(grid), len(grid[0])
        minute,fresh=0,0
        q=deque()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        
        
        while q and fresh>0:         
            for _ in range(len(q)):
                row,col=q.popleft()
                for dr, dc in directions:
                    nr,nc=row+dr,col+dc
                    if (nr in range(rows) and nc in range(cols) and (nr,nc)
                    not in visit and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
                        
            minute+=1
        return minute if fresh==0 else -1

        

        