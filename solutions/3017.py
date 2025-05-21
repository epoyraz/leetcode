class Solution(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        # count how many beautiful numbers in [1..n]
        def count(n):
            if n <= 0:
                return 0
            digs = map(int, list(str(n)))
            L = len(digs)
            memo = {}

            def dp(pos, tight, mod, diff, started):
                # diff = (#even digits) - (#odd digits)
                key = (pos, tight, mod, diff, started)
                if key in memo:
                    return memo[key]
                if pos == L:
                    # at end: must have started, divisible by k, and diff == 0
                    res = 1 if started and mod == 0 and diff == 0 else 0
                else:
                    res = 0
                    up = digs[pos] if tight else 9
                    for d in range(up + 1):
                        nt = tight and (d == up)
                        ns = started or (d != 0)
                        nm = (mod * 10 + d) % k if ns else 0
                        nd = diff
                        if ns:
                            if d % 2 == 0:
                                nd += 1
                            else:
                                nd -= 1
                        res += dp(pos + 1, nt, nm, nd, ns)
                memo[key] = res
                return res

            return dp(0, True, 0, 0, False)

        # beautifuls in [low..high] = count(high) - count(low-1)
        return count(high) - count(low - 1)
