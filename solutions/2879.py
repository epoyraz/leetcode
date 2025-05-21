class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        INF = 10**9

        # pre[i][j] = min changes to make s[i..j] a semi-palindrome
        pre = [[INF] * n for _ in range(n)]

        # helper to compute cost for substring [l,r]
        def cost_sub(l, r):
            m = r - l + 1
            best = INF
            for d in range(1, m):           # proper divisors only
                if m % d:                    # not a divisor
                    continue
                g_len = m // d
                cur = 0
                for g in range(d):           # each group 0..d-1
                    L, R = 0, g_len - 1
                    while L < R:
                        a = s[l + g + L * d]
                        b = s[l + g + R * d]
                        if a != b:
                            cur += 1
                        L += 1
                        R -= 1
                best = min(best, cur)
            return best

        # fill pre table
        for i in range(n):
            for j in range(i + 1, n):        # length at least 2
                pre[i][j] = cost_sub(i, j)

        # dp: dp[t] = min cost to split first t characters into some groups
        dp = [INF] * (n + 1)
        dp[0] = 0
        for _ in range(k):                   # perform k splits
            ndp = [INF] * (n + 1)
            for i in range(n + 1):
                if dp[i] == INF:
                    continue
                for j in range(i + 2, n + 1):   # substring length â¥2
                    c = pre[i][j - 1]
                    if c != INF:
                        ndp[j] = min(ndp[j], dp[i] + c)
            dp = ndp

        return dp[n] if dp[n] != INF else -1
