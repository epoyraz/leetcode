class Solution:
    def magicalSum(self, m, k, nums):
        mod = 10**9 + 7
        n = len(nums)
        # factorials and inverse factorials up to m
        fact = [1] * (m+1)
        for i in range(1, m+1):
            fact[i] = fact[i-1] * i % mod
        inv_fact = [1] * (m+1)
        inv_fact[m] = pow(fact[m], mod-2, mod)
        for i in range(m, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % mod
        # precompute nums[i]^c * inv_fact[c]
        pw = [[0]*(m+1) for _ in range(n)]
        for i in range(n):
            pw[i][0] = 1
            for c in range(1, m+1):
                pw[i][c] = pw[i][c-1] * nums[i] % mod
            for c in range(m+1):
                pw[i][c] = pw[i][c] * inv_fact[c] % mod
        # number of bits to process: n + enough to clear carries
        L = n + 6
        # dp[carry][ones][used]
        dp = [[[0]*(m+1) for _ in range(k+1)] for _ in range(m+1)]
        dp[0][0][0] = 1
        for i in range(L):
            ndp = [[[0]*(m+1) for _ in range(k+1)] for _ in range(m+1)]
            if i < n:
                pi = pw[i]
                for carry in range(m+1):
                    for ones in range(k+1):
                        for used in range(m+1):
                            v = dp[carry][ones][used]
                            if not v:
                                continue
                            limit = m - used
                            for c in range(limit+1):
                                s = carry + c
                                bit = s & 1
                                ones2 = ones + bit
                                if ones2 > k:
                                    continue
                                carry2 = s >> 1
                                ndp[carry2][ones2][used+c] = (
                                    ndp[carry2][ones2][used+c] + v * pi[c]
                                ) % mod
            else:
                for carry in range(m+1):
                    for ones in range(k+1):
                        for used in range(m+1):
                            v = dp[carry][ones][used]
                            if not v:
                                continue
                            s = carry
                            bit = s & 1
                            ones2 = ones + bit
                            if ones2 > k:
                                continue
                            carry2 = s >> 1
                            ndp[carry2][ones2][used] = (ndp[carry2][ones2][used] + v) % mod
            dp = ndp
        F = dp[0][k][m]
        return F * fact[m] % mod
