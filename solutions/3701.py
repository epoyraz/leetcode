import sys
class Solution(object):
    def minCostGoodCaption(self, caption):
        n = len(caption)
        INF = sys.maxint  # Python2's large int
        # Compute prefix sums of cost to change to each char c
        # pre_c[c][i] = sum of cost to change caption[0..i-1] to 'a'+c
        pre_c = [[0]*(n+1) for _ in xrange(26)]
        for c in xrange(26):
            s = 0
            for i in xrange(n):
                s += abs(ord(caption[i]) - (ord('a') + c))
                pre_c[c][i+1] = s

        # dp[i] = min cost to cover caption[0..i-1] with good blocks
        dp = [INF] * (n+1)
        dp[0] = 0
        # best[c] = min(dp[k] - pre_c[c][k]) for k <= i-3
        best = [INF] * 26
        best_k = [-1] * 26
        # For reconstruction
        prev = [-1] * (n+1)
        let = [-1] * (n+1)

        for i in xrange(1, n+1):
            # At i, before computing dp[i], update bests from k = i-3
            k = i - 3
            if k >= 0:
                for c in xrange(26):
                    val = dp[k] - pre_c[c][k]
                    if val < best[c]:
                        best[c] = val
                        best_k[c] = k
            # Compute dp[i]
            dp_i = INF
            sel_c = -1
            sel_k = -1
            if i >= 3:
                for c in xrange(26):
                    # cost for a block (k..i-1) -> char c
                    v = best[c] + pre_c[c][i]
                    if v < dp_i:
                        dp_i = v
                        sel_c = c
                        sel_k = best_k[c]
            dp[i] = dp_i
            let[i] = sel_c
            prev[i] = sel_k

        # If impossible, return empty
        if dp[n] >= INF:
            return ""
        # Reconstruct the string
        res = [''] * n
        i = n
        while i > 0:
            c = let[i]
            k = prev[i]
            # fill positions k..i-1 with char c
            for j in xrange(k, i):
                res[j] = chr(ord('a') + c)
            i = k
        return ''.join(res)
