from collections import defaultdict
import bisect

class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        # 1) Gather rows and columns
        rows = defaultdict(list)
        cols = defaultdict(list)
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)
        
        # 2) Sort each
        for x in rows:
            rows[x].sort()
        for y in cols:
            cols[y].sort()
        
        # 3) Check each building
        covered = 0
        for x, y in buildings:
            row = rows[x]
            col = cols[y]
            # Positions in the sorted lists
            i = bisect.bisect_left(row, y)
            j = bisect.bisect_left(col, x)
            
            # Need one smaller and one larger on both
            has_left  = (i > 0)
            has_right = (i < len(row) - 1)
            has_up    = (j > 0)
            has_down  = (j < len(col) - 1)
            
            if has_left and has_right and has_up and has_down:
                covered += 1
        
        return covered
