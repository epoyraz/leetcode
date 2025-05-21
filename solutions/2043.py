class Solution:
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            elems = []

            # Top row (left to right)
            for j in range(layer, n - layer):
                elems.append(grid[layer][j])
            # Right column (top to bottom)
            for i in range(layer + 1, m - layer - 1):
                elems.append(grid[i][n - layer - 1])
            # Bottom row (right to left)
            for j in range(n - layer - 1, layer - 1, -1):
                elems.append(grid[m - layer - 1][j])
            # Left column (bottom to top)
            for i in range(m - layer - 2, layer, -1):
                elems.append(grid[i][layer])

            # Rotate the elements
            k_mod = k % len(elems)
            rotated = elems[k_mod:] + elems[:k_mod]

            # Put rotated elements back
            idx = 0
            for j in range(layer, n - layer):
                grid[layer][j] = rotated[idx]
                idx += 1
            for i in range(layer + 1, m - layer - 1):
                grid[i][n - layer - 1] = rotated[idx]
                idx += 1
            for j in range(n - layer - 1, layer - 1, -1):
                grid[m - layer - 1][j] = rotated[idx]
                idx += 1
            for i in range(m - layer - 2, layer, -1):
                grid[i][layer] = rotated[idx]
                idx += 1

        return grid
