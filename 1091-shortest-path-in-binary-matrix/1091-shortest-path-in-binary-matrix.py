"""
BFS shortest path logic explained:

- BFS explores nodes in "layers" or "levels" of increasing distance from the start node.
- Initially, the queue contains only the start node at distance 1.
- At each iteration, BFS processes all nodes at the current distance before moving on to nodes at distance +1.
- This ensures that all nodes at distance k are explored before any node at distance k+1.
- Therefore, the first time we reach the target node, we have found the shortest possible path to it.
- No shorter path exists, because otherwise we would have visited the target earlier at a smaller distance layer.
- The variable tracking the current level (e.g., 'path_length') accurately reflects the shortest path length.
- This level-by-level exploration guarantees BFS finds the shortest path in unweighted grids or graphs.
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visit=set()
        directions=[[0,1],[0,-1],[1,0],[-1,0],[1,-1],[1,1],[-1,-1],[-1,1]]
        ROWS,COLS=len(grid),len(grid[0])
        path=0
        if grid[0][0]==1 or grid[ROWS-1][COLS-1]==1:
            return -1

        q=deque()
        visit.add((0,0))
        q.append((0,0))
        path=1

        while q:
            for _ in range(len(q)):
                row, col=q.popleft()
                if row==ROWS-1 and col==COLS-1:
                    return path
                for dr, dc in directions:
                    nr,nc=dr+row, dc+col
                    if ((nr,nc) not in visit and nr in range(ROWS)
                    and nc in range(COLS) and grid[nr][nc]==0):
                        visit.add((nr,nc))
                        q.append((nr,nc))
            path+=1

        return -1
    




        