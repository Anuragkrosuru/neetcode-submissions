class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        visited = set()
        
        def bfs(r, c):
            directions = [(0,1),(1,0), (-1,0), (0,-1)]

            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                x,y = q.popleft()

                for dx,dy in directions:
                    nx,ny = dx+x, dy+y
                    if (0<=nx<row and 0 <=ny<col):
                        if (grid[nx][ny]=="1" and (nx,ny) not in visited):
                            visited.add((nx,ny))
                            q.append((nx,ny))


        for i in range(row):
                for j in range(col):
                    if (grid[i][j] == "1" and (i,j) not in visited):
                        res+=1
                        bfs(i,j)
        return res