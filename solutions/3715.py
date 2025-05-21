import bisect

class Solution(object):
    def maximumCoins(self, coins, k):
        """
        :type coins: List[List[int]]
        :type k: int
        :rtype: int
        """
        # ------------------------------------------------------------------ #
        # 1. sort the (non-overlapping) segments
        coins.sort(key=lambda seg: seg[0])

        # 2. build blocks: real segments + zero-valued gaps + sentinel block
        blocks = []                      # (length, value)
        prev = 1
        for l, r, c in coins:
            if l > prev:                     # gap before this segment
                blocks.append((l - prev, 0))
            blocks.append((r - l + 1, c))    # the segment itself
            prev = r + 1
        blocks.append((k, 0))                # sentinel of length â¥ k

        # 3. prefix arrays (lengths and coin sums)
        pref_len = []
        pref_sum = []
        tot_len = tot_sum = 0
        for length, value in blocks:
            tot_len += length
            tot_sum += length * value
            pref_len.append(tot_len)
            pref_sum.append(tot_sum)

        # helper: coin total on [L, R] in O(log n)
        def range_sum(L, R):
            i = bisect.bisect_left(pref_len, L)
            j = bisect.bisect_left(pref_len, R)

            prev_L = pref_len[i - 1] if i else 0
            prev_R = pref_len[j - 1] if j else 0
            off_L  = L - prev_L - 1
            off_R  = R - prev_R - 1

            if i == j:                                   # one block only
                return (R - L + 1) * blocks[i][1]

            total  = (blocks[i][0] - off_L) * blocks[i][1]  # first block
            if j - i > 1:                                    # middle blocks
                total += pref_sum[j - 1] - pref_sum[i]
            total += (off_R + 1) * blocks[j][1]              # last block
            return total

        # 4. candidate window starts  (sentinel **included**)
        candidates = set()
        coord = 1
        for length, _ in blocks:              #  <-- sentinel not skipped
            b = coord                         # start coordinate of this block
            for x in (b, b - 1, b - k + 1, b - k):
                if x >= 1:
                    candidates.add(x)
            coord += length                   # next block
        # 5. evaluate every candidate
        best = 0
        for s in candidates:
            e = s + k - 1
            if e > tot_len:                   # window would run past sentinel
                continue
            best = max(best, range_sum(s, e))

        return best
