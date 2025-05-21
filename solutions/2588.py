class Solution:
    def maxPoints(self, grid, queries):
        m, n = len(grid), len(grid[0])
        N = m * n
        
        # Helper to convert (i, j) to 1D index
        def idx(i, j):
            return i * n + j
        
        # Create and sort list of all cells by value
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], idx(i, j)))
        cells.sort(key=lambda x: x[0])
        
        # Sort queries but remember original indices
        sorted_q = sorted((q, qi) for qi, q in enumerate(queries))
        
        # Union-Find with size
        parent = list(range(N))
        comp_size = [1] * N
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if comp_size[ra] < comp_size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            comp_size[ra] += comp_size[rb]
        
        # Active marks which cells are <= current threshold-1
        active = [False] * N
        
        answers = [0] * len(queries)
        ptr = 0  # pointer into cells
        
        # Directions for neighbors
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for qval, qidx in sorted_q:
            # Activate all cells with value < qval
            while ptr < N and cells[ptr][0] < qval:
                _, cell_i = cells[ptr]
                active[cell_i] = True
                # union with active neighbors
                i0, j0 = divmod(cell_i, n)
                for di, dj in dirs:
                    ni, nj = i0 + di, j0 + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        nb = idx(ni, nj)
                        if active[nb]:
                            union(cell_i, nb)
                ptr += 1
            
            # If start cell not active, can't move at all
            if not active[0]:
                answers[qidx] = 0
            else:
                root0 = find(0)
                answers[qidx] = comp_size[root0]
        
        return answers
