class Solution:
    def maxMoves(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            if visited[r][c] != -1:
                return visited[r][c]
            max_steps = 0
            for dr, dc in [(-1, 1), (0, 1), (1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and nc < n and grid[nr][nc] > grid[r][c]:
                    max_steps = max(max_steps, 1 + dfs(nr, nc))
            visited[r][c] = max_steps
            return max_steps

        return max(dfs(r, 0) for r in range(m))
