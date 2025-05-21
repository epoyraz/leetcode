class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        answer = []
        
        for start_col in range(n):
            col = start_col
            for row in range(m):
                dir = grid[row][col]
                next_col = col + dir
                # Check if next move goes out of bounds
                if next_col < 0 or next_col >= n:
                    col = -1
                    break
                # Check for "V" shape (mismatch in direction)
                if grid[row][next_col] != dir:
                    col = -1
                    break
                # Valid move
                col = next_col
            answer.append(col)
        
        return answer
