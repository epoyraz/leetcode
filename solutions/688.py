class Solution(object):
    def knightProbability(self, n, k, row, column):
        directions = [(-2, -1), (-2, 1), (2, -1), (2, 1),
                      (-1, -2), (-1, 2), (1, -2), (1, 2)]
        
        memo = {}
        
        def dfs(r, c, moves):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            if moves == 0:
                return 1
            if (r, c, moves) in memo:
                return memo[(r, c, moves)]
            
            prob = 0
            for dr, dc in directions:
                prob += dfs(r + dr, c + dc, moves - 1) / 8.0
            memo[(r, c, moves)] = prob
            return prob
        
        return dfs(row, column, k)
