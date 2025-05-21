class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        # DFS to mark unsurrounded 'O's (connected to border)
        def dfs(i, j):
            if (i < 0 or i >= m or j < 0 or j >= n or 
                board[i][j] != 'O'):
                return
            
            # Mark as a temporary state to avoid revisiting
            board[i][j] = 'E'  # 'E' for "escape"
            
            # Check all four directions
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # Step 1: Mark all 'O's on the border and their connected cells
        for i in range(m):
            dfs(i, 0)         # First column
            dfs(i, n-1)       # Last column
        
        for j in range(n):
            dfs(0, j)         # First row
            dfs(m-1, j)       # Last row
        
        # Step 2: Capture surrounded regions and restore unsurrounded ones
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    # This 'O' is surrounded, capture it
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    # This 'O' was connected to the border, restore it
                    board[i][j] = 'O'