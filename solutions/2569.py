class Solution:
    def beautifulPartitions(self, s, k, minLength):
        MOD = 10**9 + 7
        n = len(s)
        primes = set('2357')

        # Quick sanity checks
        if s[0] not in primes or s[-1] in primes:
            return 0

        # Precompute start/end validity arrays
        is_start = [c in primes for c in s]
        is_end   = [c not in primes for c in s]

        # dp[i][j]: number of ways to partition s[i:] into exactly j pieces
        # We only need dp[*][j-1] to compute dp[*][j], so roll by j
        dp_prev = [0] * (n + 1)
        dp_prev[n] = 1  # base: one way to partition empty suffix into 0 pieces

        for pieces in range(1, k + 1):
            # Build suffix-sum array of dp_prev[x] but only where x-1 is valid end
            # suf[i] = sum(dp_prev[x] for x=i..n if x>i and is_end[x-1])
            suf = [0] * (n + 2)
            for i in range(n, -1, -1):
                val = dp_prev[i] if (1 <= i <= n and is_end[i-1]) else 0
                suf[i] = (val + suf[i + 1]) % MOD

            # Compute dp_curr
            dp_curr = [0] * (n + 1)
            for i in range(n):
                if is_start[i]:
                    j = i + minLength
                    if j <= n:
                        dp_curr[i] = suf[j]
            # dp_curr[n] stays zero for pieces>=1
            dp_prev = dp_curr

        # Answer: ways to partition full string s[0:] into k pieces
        return dp_prev[0] % MOD
