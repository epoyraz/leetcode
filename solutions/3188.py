class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # A team a is champion iff no other team b is stronger:
        # i.e. there is no b with grid[b][a] == 1.
        for a in range(n):
            for b in range(n):
                if grid[b][a] == 1:
                    break
            else:
                # no break => no b stronger than a
                return a
        # problem guarantees a unique champion, so we never reach here
        return -1