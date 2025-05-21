class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        index = 2
        area = {}
        
        def dfs(x, y, idx):
            if x < 0 or y < 0 or x >= n or y >= n or grid[x][y] != 1:
                return 0
            grid[x][y] = idx
            return 1 + dfs(x+1, y, idx) + dfs(x-1, y, idx) + dfs(x, y+1, idx) + dfs(x, y-1, idx)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = dfs(i, j, index)
                    index += 1
        
        res = max(area.values() or [0])
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        ni, nj = i+dx, j+dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen.add(grid[ni][nj])
                    res = max(res, 1 + sum(area[idx] for idx in seen))
        
        return res
