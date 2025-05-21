class Solution(object):
    def colorTheGrid(self, m, n):
        MOD = 10**9+7
        total = 3**m
        valid = []
        cols = []
        for p in range(total):
            x = p
            prev = -1
            ok = True
            col = []
            for _ in range(m):
                d = x % 3
                x //= 3
                if d == prev:
                    ok = False
                    break
                prev = d
                col.append(d)
            if ok:
                valid.append(p)
                cols.append(col)
        k = len(valid)
        comp = [[False]*k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                ok = True
                for r in range(m):
                    if cols[i][r] == cols[j][r]:
                        ok = False
                        break
                comp[i][j] = ok
        dp = [1]*k
        for _ in range(1, n):
            ndp = [0]*k
            for j in range(k):
                s = 0
                for i in range(k):
                    if comp[i][j]:
                        s += dp[i]
                ndp[j] = s % MOD
            dp = ndp
        return sum(dp) % MOD
