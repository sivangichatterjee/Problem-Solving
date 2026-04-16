class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols=len(image),len(image[0])
        original=image[sr][sc]
        if original==color:
            return image
        q=deque()
        q.append((sr,sc))
        image[sr][sc]=color
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            row,col=q.popleft()
            for dr,dc in directions:
                nr,nc=dr+row,dc+col
                if 0<=nr<rows and 0<=nc<cols and image[nr][nc]==original:
                    image[nr][nc]=color
                    q.append((nr,nc))

        return image
                
                


