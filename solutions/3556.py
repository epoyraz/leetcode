MOD = 1000000007          # modulus

class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        if k == 0 or multiplier == 1:
            return [x % MOD for x in nums]

        import math
        n     = len(nums)
        log_m = math.log(multiplier)
        exp0  = [math.log(x) / log_m for x in nums]   # fractional exponents

        # -------- 1. binary-search the smallest integer E with â¥ k terms -----
        def count_leq(E):
            tot = 0
            for e in exp0:
                if E + 1e-12 >= e:                    # small guard
                    tot += int(E - e) + 1
            return tot

        lo = int(min(exp0))
        hi = lo + k                                   # safe upper bound
        while lo < hi:
            mid = (lo + hi) // 2
            if count_leq(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        E = lo                                        # final threshold

        # -------- 2. counts up to E and the "last picked" value --------------
        cnt   = [0] * n
        total = 0
        tails = []                                    # (last_value, index)

        for i, e in enumerate(exp0):
            if E + 1e-12 >= e:
                c = int(E - e) + 1
                cnt[i] = c
                total += c
                tails.append((e + (c - 1), i))        # last exponent

        # -------- 3. drop the 'excess' largest tails (value, then index) -----
        excess = total - k
        if excess:
            tails.sort(key=lambda p: (-p[0], -p[1]))  # descending
            for _, idx in tails[:excess]:
                cnt[idx] -= 1

        # -------- 4. rebuild the array under the modulus ---------------------
        mm = multiplier % MOD
        return [(x % MOD) * pow(mm, c, MOD) % MOD for x, c in zip(nums, cnt)]
