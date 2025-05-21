MOD = 10 ** 9 + 7

class Solution(object):
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        n  = len(nums)
        if n == 1:
            return 0                          # already equal

        s  = sum(nums)
        mn = min(nums)
        mx = max(nums)

        # âââââââââââââââââââââââââââ simple cases ââââââââââââââââââââââââââââ
        if cost2 >= 2 * cost1:                # pair not cheaper than singles
            return ((n * mx - s) * cost1) % MOD
        if n == 2:                            # pairs never help with two items
            return abs(nums[0] - nums[1]) * cost1 % MOD

        # âââââââââââââââââââââ cost for a particular target T âââââââââââââââââ
        def raw_cost(T):
            S = n * T - s                     # total units still missing
            singles = max(0, (s - 2 * mn) - (n - 2) * T)  # 2Â·M â S
            if (S - singles) & 1:             # need even remainder for pairs
                singles += 1
            pairs = (S - singles) // 2
            return singles * cost1 + pairs * cost2  # *raw* cost, no modulo

        # slope while singles_needed > 0
        slope1 = (n - 1) * cost2 - (n - 2) * cost1

        cand = set([mx])                      # always test the current max

        if slope1 < 0:                        # V-shape, vertex to the right
            num = s - 2 * mn
            den = n - 2                       # n â¥ 3 here, so den > 0

            t_floor = max(mx, num // den)                 # âTââ
            t_ceil  = max(mx, (num + den - 1) // den)     # âTââ

            cand.update([t_floor, t_ceil, t_ceil + 1])    # +1 covers dip
            if t_floor - 1 >= mx:                         # rarely useful
                cand.add(t_floor - 1)
        else:                              # cost already increasing at mx
            cand.add(mx + 1)               # parity dip can be right after mx

        # evaluate â¤ 5 candidates, pick the true minimum, *then* apply modulo
        best_raw = min(raw_cost(T) for T in cand)
        return best_raw % MOD
