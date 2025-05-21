class Solution:
    def matrixRankTransform(self, matrix):
        m, n = len(matrix), len(matrix[0])
        # Prepare list of (value, row, col)
        cells = [(matrix[i][j], i, j) for i in range(m) for j in range(n)]
        cells.sort(key=lambda x: x[0])
        
        # Track the maximum rank assigned so far for each row and column
        row_max = [0]*m
        col_max = [0]*n
        
        # The answer matrix
        answer = [[0]*n for _ in range(m)]
        
        # Union-Find helper
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx
        
        # Process cells in increasing value order, grouping equal values
        i = 0
        N = m*n
        while i < N:
            # Gather all cells with the same value
            v = cells[i][0]
            j = i
            while j < N and cells[j][0] == v:
                j += 1
            
            # DSU over this batch of cells: indices 0..(j-i-1)
            size = j - i
            parent = list(range(size))
            
            # Map row -> index in this batch, col -> index
            row_rep = {}
            col_rep = {}
            
            for k in range(size):
                _, r, c = cells[i + k]
                if r in row_rep:
                    union(row_rep[r], k)
                else:
                    row_rep[r] = k
                if c in col_rep:
                    union(col_rep[c], k)
                else:
                    col_rep[c] = k
            
            # For each group root, collect its cells
            groups = {}
            for k in range(size):
                root = find(k)
                groups.setdefault(root, []).append(k)
            
            # Compute and assign ranks for each group
            for group in groups.values():
                # Determine the rank base from max of row_max and col_max
                best_prev = 0
                for k in group:
                    _, r, c = cells[i + k]
                    best_prev = max(best_prev, row_max[r], col_max[c])
                rank = best_prev + 1
                # Assign and update row_max, col_max
                for k in group:
                    _, r, c = cells[i + k]
                    answer[r][c] = rank
                    row_max[r] = max(row_max[r], rank)
                    col_max[c] = max(col_max[c], rank)
            
            i = j
        
        return answer
