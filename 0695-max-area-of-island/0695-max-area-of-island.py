class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visit=set()
        maxarea=0
        rows, cols=len(grid), len(grid[0])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        def bfs(r,c):
            q=deque()
            visit.add((r,c))
            q.append((r,c))
            area=1           
            while q:
                row, col=q.popleft()              
                for dr, dc in directions:
                    nr,nc=row+dr, col+dc
                    if ((nr,nc) not in visit and 
                    nr in range(rows) and 
                    nc in range(cols) and 
                    grid[nr][nc]==1):
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        area+=1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:                   
                    maxarea=max(maxarea, bfs(r,c))

        return maxarea


        