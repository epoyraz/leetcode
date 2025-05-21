class Solution(object):
    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])
        
        parent = [i for i in range(m * n + 1)]
        size = [1] * (m * n + 1)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr:
                return
            parent[xr] = yr
            size[yr] += size[xr]
        
        def idx(x, y):
            return x * n + y
        
        # Mark bricks to be removed
        for x, y in hits:
            if grid[x][y] == 1:
                grid[x][y] = 2
        
        # Connect the grid initially
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0:
                        union(idx(i,j), m*n)
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        ni, nj = i+dx, j+dy
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                            union(idx(i,j), idx(ni,nj))
        
        res = []
        for x, y in reversed(hits):
            prev = size[find(m*n)]
            if grid[x][y] == 0:
                res.append(0)
                continue
            grid[x][y] = 1
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = x+dx, y+dy
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    union(idx(x,y), idx(ni,nj))
            if x == 0:
                union(idx(x,y), m*n)
            curr = size[find(m*n)]
            res.append(max(0, curr - prev - 1))
        
        return res[::-1]
