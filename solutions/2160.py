class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        flat = []
        for row in grid:
            for val in row:
                flat.append(val)

        base = flat[0] % x
        for val in flat:
            if val % x != base:
                return -1

        flat.sort()
        median = flat[len(flat) // 2]

        operations = 0
        for val in flat:
            operations += abs(val - median) // x

        return operations
