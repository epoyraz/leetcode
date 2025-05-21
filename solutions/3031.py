class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        # Flatten grid
        n = len(grid)
        m = len(grid[0])
        N = n * m
        A = [0] * N
        idx = 0
        for i in range(n):
            for j in range(m):
                A[idx] = grid[i][j] % MOD
                idx += 1

        # Prefix products
        P = [1] * (N + 1)
        for i in range(N):
            P[i+1] = (P[i] * A[i]) % MOD

        # Suffix products
        S = [1] * (N + 1)
        for i in range(N - 1, -1, -1):
            S[i] = (S[i+1] * A[i]) % MOD

        # Build result
        res = [[0] * m for _ in range(n)]
        idx = 0
        for i in range(n):
            for j in range(m):
                res[i][j] = (P[idx] * S[idx+1]) % MOD
                idx += 1

        return res
