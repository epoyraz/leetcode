class Solution:
    def waysToFillArray(self, queries):
        mod = 10**9 + 7
        max_n = max(n for n, k in queries)
        max_k = max(k for n, k in queries)
        MAX = max_n + 14

        # factorials and inverse factorials
        f = [1] * (MAX + 1)
        for i in range(1, MAX + 1):
            f[i] = f[i-1] * i % mod
        invf = [1] * (MAX + 1)
        invf[MAX] = pow(f[MAX], mod-2, mod)
        for i in range(MAX, 0, -1):
            invf[i-1] = invf[i] * i % mod

        # smallest prime factor sieve
        N = max_k
        spf = list(range(N+1))
        for i in range(2, int(N**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, N+1, i):
                    if spf[j] == j:
                        spf[j] = i

        def factor(k):
            d = {}
            while k > 1:
                p = spf[k]
                cnt = 0
                while k % p == 0:
                    k //= p
                    cnt += 1
                d[p] = cnt
            return d

        ans = []
        for n, k in queries:
            ways = 1
            for e in factor(k).values():
                ways = ways * (f[n+e-1] * invf[e] % mod * invf[n-1] % mod) % mod
            ans.append(ways)
        return ans
