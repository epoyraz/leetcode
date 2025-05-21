class Solution(object):
    def canMakeSquare(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        # There are four 2x2 sub-squares in a 3x3 grid
        for i in range(2):
            for j in range(2):
                # count 'B' and 'W' in this 2x2
                b = 0
                w = 0
                for di in (0, 1):
                    for dj in (0, 1):
                        if grid[i+di][j+dj] == 'B':
                            b += 1
                        else:
                            w += 1
                # if we can change at most one cell, we need either 4 or 3 of one color
                if b >= 3 or w >= 3:
                    return True
        return False