class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def dfs(r, c):
            stack = [(r, c)]
            visited[r][c] = True
            total = 0
            while stack:
                x, y = stack.pop()
                total += grid[x][y]
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] > 0:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            return total
        
        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    max_fish = max(max_fish, dfs(i, j))
        return max_fish