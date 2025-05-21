class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        count = [0] * (n * n + 1)
        
        # Count frequency of each number in the grid
        for row in grid:
            for val in row:
                count[val] += 1
        
        repeated = missing = -1
        for i in range(1, n * n + 1):
            if count[i] == 2:
                repeated = i
            elif count[i] == 0:
                missing = i
        
        return [repeated, missing]
