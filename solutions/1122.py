class Solution:
    def longestDupSubstring(self, s):
        n = len(s)
        nums = [ord(c) - 97 for c in s]   # map a..z to 0..25
        mod1, mod2 = 10**9 + 7, 10**9 + 9
        base = 26

        # pre-compute powers
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * base) % mod1
            pow2[i] = (pow2[i - 1] * base) % mod2

        def check(L):
            """return start index of a duplicate substring of length L or -1"""
            h1 = h2 = 0
            for i in range(L):
                h1 = (h1 * base + nums[i]) % mod1
                h2 = (h2 * base + nums[i]) % mod2
            seen = {(h1, h2)}
            for i in range(L, n):
                h1 = (h1 * base - nums[i - L] * pow1[L] + nums[i]) % mod1
                h2 = (h2 * base - nums[i - L] * pow2[L] + nums[i]) % mod2
                key = (h1, h2)
                if key in seen:
                    return i - L + 1
                seen.add(key)
            return -1

        lo, hi, idx = 1, n - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            pos = check(mid)
            if pos != -1:
                lo, idx, best = mid + 1, pos, mid
            else:
                hi = mid - 1
        return "" if idx == -1 else s[idx:idx + best]
