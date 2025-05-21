class Solution(object):
    def countOfPairs(self, n, x, y):
        # same-house shortcut â simple line
        if x == y:
            return [(n - k) * 2 for k in xrange(1, n + 1)]

        # keep  x < y
        if x > y:
            x, y = y, x

        # unordered baseline: pure line
        cnt = [n - d for d in xrange(1, n)] + [0]

        a, b       = x, y          # chord endpoints (a < b)
        mid_limit  = (a + b - 2) // 2      # max i we need to look at

        add = [0] * (n + 2)        # range-adds for new   distances
        sub = [0] * (n + 2)        # range-subs for old   distances

        for i in xrange(1, mid_limit + 1):
            A = abs(i - a) + 1     # fixed prefix length to reach the chord

            # ---- j  â¥  b  ----------------------------------------------
            k1, k2 = A, A + (n - b)        # new-distance range
            d1, d2 = b - i, n - i          # old-distance range
            add[k1]           += 1
            add[min(k2 + 1, n + 1)] -= 1
            sub[d1]           += 1
            sub[d2 + 1]       -= 1

            # ---- i+1 â¤ j < b  (but large enough to make the shortcut best)
            thresh  = (i + b + A) // 2 + 1
            j_low   = max(i + 1, thresh)
            if j_low < b:
                k_low, k_high = A + 1, A + b - j_low
                d_low, d_high = j_low - i, (b - 1) - i
                add[k_low]                += 1
                add[min(k_high + 1, n + 1)] -= 1
                sub[d_low]                += 1
                sub[d_high + 1]           -= 1

        # apply the difference arrays
        cur = 0
        for k in xrange(1, n + 1):
            cur += add[k]
            cnt[k - 1] += cur
        cur = 0
        for k in xrange(1, n + 1):
            cur += sub[k]
            cnt[k - 1] -= cur

        # convert unordered â ordered
        return [v * 2 for v in cnt]
