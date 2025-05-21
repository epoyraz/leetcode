class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        if not grid or not grid[0]:
            return []

        m, n = len(grid), len(grid[0])
        result = []

        for col in range(n):
            max_width = 0
            for row in range(m):
                width = len(str(grid[row][col]))
                max_width = max(max_width, width)
            result.append(max_width)

        return result
