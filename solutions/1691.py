class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        def count_islands():
            seen = [[False]*n for _ in range(m)]
            def dfs(i, j):
                stack = [(i,j)]
                seen[i][j] = True
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < m and 0 <= ny < n \
                           and grid[nx][ny] == 1 and not seen[nx][ny]:
                            seen[nx][ny] = True
                            stack.append((nx, ny))
            
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not seen[i][j]:
                        islands += 1
                        dfs(i, j)
            return islands
        
        # Step 1: if already disconnected
        if count_islands() != 1:
            return 0
        
        # Step 2: try removing one land cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        
        # Step 3: otherwise, needs two removals
        return 2
