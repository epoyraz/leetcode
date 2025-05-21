class Solution(object):
    def minimumMoves(self, grid):
        # Flatten initial stones: list of (r,c), length 9
        stones = []
        for r in range(3):
            for c in range(3):
                for _ in range(grid[r][c]):
                    stones.append((r, c))
        # Must have exactly 9 stones
        # Targets: one per cell
        targets = [(r, c) for r in range(3) for c in range(3)]
        
        N = 9
        FULL = (1 << N) - 1
        # dp[mask] = minimal cost assigning first popcount(mask) stones to targets in mask
        dp = [float('inf')] * (1 << N)
        dp[0] = 0
        
        for mask in range(1 << N):
            k = bin(mask).count('1')  # number of stones already assigned
            if k >= N:
                continue
            sr, sc = stones[k]
            # try assign k-th stone to any free target j
            for j in range(N):
                if not (mask & (1 << j)):
                    tr, tc = targets[j]
                    cost = abs(sr - tr) + abs(sc - tc)
                    nxt = mask | (1 << j)
                    if dp[mask] + cost < dp[nxt]:
                        dp[nxt] = dp[mask] + cost
        
        return dp[FULL]
