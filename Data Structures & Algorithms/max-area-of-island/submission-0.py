class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(r, c):
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            count = 1
            while q:
                x,y = q.popleft()
                for dx,dy in directions:
                    nx, ny = x+dx, y+dy
                    if (0 <= nx < row and 0 <= ny < col and
                        grid[nx][ny] == 1 and (nx,ny) not in visited):
                        visited.add((nx,ny))
                        q.append((nx,ny))
                        count+=1
            return count
                

        # Traverse the grid
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    res= max(res, bfs(i,j))

        return res