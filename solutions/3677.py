class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        m = len(coins)
        n = len(coins[0])
        # Use a very large negative for -infinity
        NEG_INF = -10**18
        # dp[i][j][k]: max coins at (i,j) having used k neutralizations
        dp = [[[NEG_INF] * 3 for _ in range(n)] for __ in range(m)]
        # Initialize start cell (0,0)
        start = coins[0][0]
        if start >= 0:
            dp[0][0][0] = start
        else:
            # without using neutralization
            dp[0][0][0] = start
            # use one neutralization here
            dp[0][0][1] = 0
        # Fill first row
        for j in range(1, n):
            val = coins[0][j]
            for k in range(3):
                prev = dp[0][j-1][k]
                if prev == NEG_INF:
                    continue
                # take cell normally
                dp[0][j][k] = max(dp[0][j][k], prev + val)
                # if it's a robber, try neutralizing
                if val < 0 and k + 1 < 3:
                    dp[0][j][k+1] = max(dp[0][j][k+1], prev)
        # Fill first column
        for i in range(1, m):
            val = coins[i][0]
            for k in range(3):
                prev = dp[i-1][0][k]
                if prev == NEG_INF:
                    continue
                dp[i][0][k] = max(dp[i][0][k], prev + val)
                if val < 0 and k + 1 < 3:
                    dp[i][0][k+1] = max(dp[i][0][k+1], prev)
        # Fill interior cells
        for i in range(1, m):
            for j in range(1, n):
                val = coins[i][j]
                for k in range(3):
                    # non-neutral transition
                    best_prev = NEG_INF
                    up = dp[i-1][j][k]
                    left = dp[i][j-1][k]
                    if up != NEG_INF:
                        best_prev = max(best_prev, up)
                    if left != NEG_INF:
                        best_prev = max(best_prev, left)
                    if best_prev != NEG_INF:
                        dp[i][j][k] = max(dp[i][j][k], best_prev + val)
                    # neutralize if robber and we have neutralizations left
                    if val < 0 and k > 0:
                        prev_neut = NEG_INF
                        upn = dp[i-1][j][k-1]
                        lfn = dp[i][j-1][k-1]
                        if upn != NEG_INF:
                            prev_neut = max(prev_neut, upn)
                        if lfn != NEG_INF:
                            prev_neut = max(prev_neut, lfn)
                        if prev_neut != NEG_INF:
                            dp[i][j][k] = max(dp[i][j][k], prev_neut)
        # The result is the best we can do at the bottom-right with up to 2 neutrals
        return max(dp[m-1][n-1])