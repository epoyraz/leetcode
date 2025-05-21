from collections import deque

class Solution(object):
    def maxMoves(self, kx, ky, positions):
        n = len(positions)
        # include the knight's start as point n
        pts = positions + [(kx, ky)]
        N = n + 1

        # Precompute knight distances between all pts[i] -> pts[j]
        dist = [[0]*N for _ in range(N)]
        dirs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        for i, (sx, sy) in enumerate(pts):
            D = [[-1]*50 for _ in range(50)]
            dq = deque([(sx, sy)])
            D[sx][sy] = 0
            while dq:
                x, y = dq.popleft()
                d0 = D[x][y]
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and D[nx][ny] < 0:
                        D[nx][ny] = d0 + 1
                        dq.append((nx, ny))
            for j, (tx, ty) in enumerate(pts):
                dist[i][j] = D[tx][ty]

        full = (1<<n) - 1
        # dp[mask][cur]: optimal total from state
        dp = [[0]*N for _ in range(1<<n)]
        # base dp[0][*] = 0

        for mask in range(1, full+1):
            # number removed so far = n - popcount(mask)
            removed = n - bin(mask).count('1')
            alice = (removed % 2 == 0)
            for cur in range(N):
                if alice:
                    best = -10**18
                else:
                    best =  10**18
                m = mask
                while m:
                    lb = m & -m
                    i = (lb.bit_length() - 1)
                    m ^= lb
                    nxt = mask ^ lb
                    cost = dist[cur][i] + dp[nxt][i]
                    if alice:
                        if cost > best: best = cost
                    else:
                        if cost < best: best = cost
                dp[mask][cur] = best

        return dp[full][n]
