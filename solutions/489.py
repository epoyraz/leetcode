class Solution:
    def kthSmallestPath(self, destination, k):
        row, col = destination
        # Precompute nCk up to n = row+col (max 30)
        n = row + col
        C = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            C[i][0] = 1
            for j in range(1, i+1):
                C[i][j] = C[i-1][j-1] + C[i-1][j]
        
        path = []
        # Build the path character by character
        for _ in range(n):
            if col == 0:
                # No H left, must put V
                path.append('V')
                row -= 1
            elif row == 0:
                # No V left, must put H
                path.append('H')
                col -= 1
            else:
                # Count of strings if we put 'H' next:
                # we then need to arrange (col-1) H's and row V's over (row+col-1) positions
                cnt = C[row+col-1][row]
                if k <= cnt:
                    path.append('H')
                    col -= 1
                else:
                    path.append('V')
                    k -= cnt
                    row -= 1
        
        return ''.join(path)
