class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        top = grid[0][:]
        bottom = grid[1][:]
        
        # Prefix sums for easy range sum calculation
        for i in range(1, n):
            top[i] += top[i - 1]
            bottom[i] += bottom[i - 1]
        
        result = float('inf')
        
        for i in range(n):
            # If first robot drops down at column i:
            # Top remaining for robot 2 is from i+1 to n-1
            top_remain = top[-1] - top[i] if i < n - 1 else 0
            # Bottom remaining for robot 2 is from 0 to i-1
            bottom_remain = bottom[i - 1] if i > 0 else 0
            result = min(result, max(top_remain, bottom_remain))
        
        return result
