class Solution(object):
    def squareFreeSubsets(self, nums):
        MOD = 10**9 + 7
        from collections import Counter
        freq = Counter(nums)
        ones = freq.get(1, 0)

        # primes up to 30 that appear in square-free numbers
        primes = [2,3,5,7,11,13,17,19,23,29]

        # build mask of prime factors for each candidate x > 1 that is square-free
        pfmask = {}
        for x, cnt in freq.items():
            if x == 1:
                continue
            # skip if x has a squared prime factor
            if x % 4 == 0 or x % 9 == 0 or x % 16 == 0 or x % 25 == 0:
                continue
            m = 0
            for i, p in enumerate(primes):
                if x % p == 0:
                    m |= 1 << i
            pfmask[x] = m

        # dp[mask] = #ways to pick a subset of types with combined primeâmask == mask
        dp = [0] * (1 << len(primes))
        dp[0] = 1

        for x, m in pfmask.items():
            cnt = freq[x]
            new_dp = dp[:]  # copy old
            for mask in range(len(dp)):
                if dp[mask] and (mask & m) == 0:
                    new_dp[mask | m] = (new_dp[mask | m] + dp[mask] * cnt) % MOD
            dp = new_dp

        # K = total ways including empty subset
        K = sum(dp) % MOD

        # each subset of non-ones can be paired with any subset of ones:
        pow2 = pow(2, ones, MOD)

        # subtract 1 to exclude the all-empty subset
        return (K * pow2 - 1) % MOD
