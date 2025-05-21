class Solution:
    def numberOfGoodSubsets(self, nums):
        mod = 10**9 + 7
        from collections import Counter

        freq = Counter(nums)
        # List of primes <= 30
        primes = [2,3,5,7,11,13,17,19,23,29]
        # Map prime to bit position
        p2bit = {p:i for i,p in enumerate(primes)}

        # Precompute mask for each x in [2..30] if square-free; else mask = 0 (invalid)
        mask = [0]*31
        for x in range(2,31):
            m = 0
            y = x
            ok = True
            for p in primes:
                if p*p > y:
                    break
                if y % p == 0:
                    cnt = 0
                    while y % p == 0:
                        y //= p
                        cnt += 1
                    if cnt > 1:
                        ok = False
                        break
                    m |= 1 << p2bit[p]
            if not ok:
                continue
            # y is 1 or a prime > sqrt(x)
            if y > 1:
                if y not in p2bit:
                    # prime > 30? won't happen
                    ok = False
                else:
                    # ensure it appears only once
                    m |= 1 << p2bit[y]
            if ok:
                mask[x] = m

        # dp over prime-masks
        M = 1 << len(primes)   # 2^10 = 1024
        dp = [0]*M
        dp[0] = 1

        # For each x > 1 with freq and valid mask
        for x in range(2,31):
            m = mask[x]
            c = freq.get(x, 0)
            if c == 0 or m == 0:
                continue
            # update dp from high to low
            for pm in range(M-1, -1, -1):
                if dp[pm] and (pm & m) == 0:
                    dp[pm | m] = (dp[pm | m] + dp[pm] * c) % mod

        # Sum all non-zero masks
        total = sum(dp[1:]) % mod

        # Factor in 1's: each good subset can include any subset of 1's
        ones = freq.get(1, 0)
        if ones:
            total = total * pow(2, ones, mod) % mod

        return total
