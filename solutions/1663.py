class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    char = grid[i][j]
                    visited[i][j] = True
                    stack = [(i, j, -1, -1)]  # (row, col, parent_row, parent_col)
                    while stack:
                        r, c, pr, pc = stack.pop()
                        for dr, dc in dirs:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == char:
                                if not visited[nr][nc]:
                                    visited[nr][nc] = True
                                    stack.append((nr, nc, r, c))
                                elif not (nr == pr and nc == pc):
                                    # Found a cycle
                                    return True
        return False
