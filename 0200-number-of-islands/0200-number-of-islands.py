class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        islands=0
        visit=set()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        def bfs(r,c):
            q=deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    nr,nc=dr+row,dc+col
                    if(nr in range(rows) and nc in range(cols) and (nr,nc) not in visit 
                    and grid[nr][nc]=="1"):
                        q.append((nr,nc))
                        visit.add((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visit:
                    bfs(i,j)
                    islands+=1

        return islands

        




        