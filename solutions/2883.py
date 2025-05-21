class Solution:
    def minimumBeautifulSubstrings(self, s):
        # Precompute all binary strings of powers of 5 up to length 15
        powers_of_5 = set()
        val = 1
        while val < (1 << 15):
            powers_of_5.add(bin(val)[2:])
            val *= 5

        memo = {}

        def dp(i):
            if i == len(s):
                return 0
            if s[i] == '0':  # no leading zero allowed
                return float('inf')
            if i in memo:
                return memo[i]

            res = float('inf')
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in powers_of_5:
                    res = min(res, 1 + dp(j))

            memo[i] = res
            return res

        ans = dp(0)
        return ans if ans != float('inf') else -1
