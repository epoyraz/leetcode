class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        if m == 0:
            return []
        flat = []
        for i in range(m):
            row = grid[i]
            if i % 2 == 1:
                row = row[::-1]
            flat.extend(row)
        # skip every alternate: take even indices
        return flat[::2]
