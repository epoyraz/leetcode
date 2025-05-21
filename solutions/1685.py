import bisect

class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        if n < 2:
            return 0

        # 1) prefix sums so any sum(i..j) is prefix[j+1]-prefix[i]
        prefix = [0]*(n+1)
        for i, v in enumerate(stoneValue):
            prefix[i+1] = prefix[i] + v

        # 2) dp[i][j] = best score for subarray stoneValue[i..j]
        dp = [[0]*n for _ in range(n)]

        # 3) bestLeft[i][k] = max over t in [i..k] of (prefix[t+1] + dp[i][t])
        bestLeft = [[float('-inf')]*n for _ in range(n)]
        for i in range(n):
            bestLeft[i][i] = prefix[i+1]  # dp[i][i]=0

        # 4) fill by increasing j, and for each j scan i downward
        for j in range(1, n):
            # suffixBest[t] = max(dp[t][j] - prefix[t]) for t in [..j]
            # we build it on the fly as i goes down
            suffixBest = [float('-inf')] * (n+2)
            suffixBest[j] = dp[j][j] - prefix[j]   # = -prefix[j]
            suffixBest[j+1] = float('-inf')

            for i in range(j-1, -1, -1):
                # incorporate dp[i+1][j] into suffixBest[i+1]
                val = dp[i+1][j] - prefix[i+1]
                old = suffixBest[i+2]
                suffixBest[i+1] = val if val > old else old

                # find splitâpoint pivot k0 by binary search:
                # first u in [i+1..j] with prefix[u] - prefix[i] >= prefix[j+1] - prefix[u]
                S = prefix[j+1] + prefix[i]
                M = (S + 1)//2
                # prefix[u] >= M  â  left(u-1) >= right(u-1)
                u = bisect.bisect_left(prefix, M, i+1, j+1)

                best = 0
                # A1: splits k where left<right â k â¤ u-2
                left_end = u - 2
                if left_end >= i:
                    tmp = bestLeft[i][left_end] - prefix[i]
                    if tmp > best:
                        best = tmp

                # A2: splits k where left>right or = â consider right+dp, t=k+1 â¥ u
                if u <= j:
                    # right side best: prefix[j+1] + max(dp[t][j] - prefix[t]) for t â¥ u
                    tmp = prefix[j+1] + suffixBest[u]
                    if tmp > best:
                        best = tmp
                    # A3: if there is an *equal* split at k_eq=u-1
                    if 2*prefix[u] == S:
                        left_k = prefix[u] - prefix[i]
                        # Alice can also discard *right*, so
                        tmp2 = left_k + dp[i][u-1]
                        if tmp2 > best:
                            best = tmp2

                dp[i][j] = best
                # update bestLeft[i][j]
                prev = bestLeft[i][j-1]
                cand = prefix[j+1] + best
                bestLeft[i][j] = cand if cand > prev else prev

        return dp[0][n-1]
