class Solution:
    def colorBorder(self, grid, row, col, color):
        m, n = len(grid), len(grid[0])
        orig = grid[row][col]
        visited = set()
        stack = [(row, col)]
        
        # DFS to find the connected component
        while stack:
            i, j = stack.pop()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == orig:
                    stack.append((ni, nj))
        
        # Identify border cells
        border = set()
        for i, j in visited:
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                border.add((i, j))
            else:
                for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni, nj = i + di, j + dj
                    if (ni, nj) not in visited:
                        border.add((i, j))
                        break
        
        # Color the border
        for i, j in border:
            grid[i][j] = color
        
        return grid
