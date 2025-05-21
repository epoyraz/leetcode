class Solution:
    def countUnguarded(self, m, n, guards, walls):
        total = m * n
        # 0 = empty, 1 = guard, 2 = wall, 3 = guarded
        grid = [0] * total
        
        # Place guards and walls
        for r, c in guards:
            grid[r*n + c] = 1
        for r, c in walls:
            grid[r*n + c] = 2
        
        # Helper to sweep a line of indices in 'grid'
        def sweep_line(idxs):
            seen = False
            for idx in idxs:
                cell = grid[idx]
                if cell == 2:        # wall
                    seen = False
                elif cell == 1:      # guard
                    seen = True
                elif cell == 0 and seen:
                    grid[idx] = 3     # mark as guarded
        
        # Sweep each row leftâright and rightâleft
        for r in range(m):
            base = r * n
            row_idxs = [base + c for c in range(n)]
            sweep_line(row_idxs)
            sweep_line(row_idxs[::-1])
        
        # Sweep each column topâdown and bottomâup
        for c in range(n):
            col_idxs = [r*n + c for r in range(m)]
            sweep_line(col_idxs)
            sweep_line(col_idxs[::-1])
        
        # Count unguarded empty cells
        ans = 0
        for v in grid:
            if v == 0:
                ans += 1
        return ans
