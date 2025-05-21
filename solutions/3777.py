class Solution(object):
    def maxProduct(self, nums, k, limit):
        # dp_pos[(sum,parity)] = set of all positive products â¤limit reaching that state WITHOUT any zero
        dp_pos = {}
        best_pos = -1

        # dp_sums = set of all (sum,parity) reachable ignoring product entirely
        # dp_zero = set of all (sum,parity) reachable with at least one zero (product=0)
        dp_sums = set()
        dp_zero = set()
        zero_ok = False

        for v in nums:
            new_sums = set()
            new_pos  = {}
            new_zero = set()

            # 1) Handle positive v
            if v != 0:
                # start a new subsequence [v]
                new_sums.add((v, 1))
                if v <= limit:
                    new_pos.setdefault((v, 1), set()).add(v)
                    if v == k:
                        best_pos = max(best_pos, v)

                # extend every old sum state (for future zero-collapses and dp_sums)
                for (s, p) in dp_sums:
                    s2 = s + v if p == 0 else s - v
                    p2 = 1 - p
                    new_sums.add((s2, p2))

                # extend every positive path
                for (s, p), prods in dp_pos.items():
                    s2 = s + v if p == 0 else s - v
                    p2 = 1 - p
                    cap = limit // v
                    for prod in prods:
                        if prod <= cap:
                            p2val = prod * v
                            if p2val <= limit:
                                new_pos.setdefault((s2, p2), set()).add(p2val)
                                if s2 == k:
                                    best_pos = max(best_pos, p2val)

                # extend zero-layer forward (still product=0)
                for (s, p) in dp_zero:
                    s2 = s + v if p == 0 else s - v
                    p2 = 1 - p
                    new_zero.add((s2, p2))
                    if s2 == k:
                        zero_ok = True

            # 2) Handle v == 0
            else:
                # start [0]
                new_sums.add((0, 1))
                new_zero.add((0, 1))
                if k == 0:
                    zero_ok = True

                # *collapse* every previously reachable sum into the zero-layer
                for (s, p) in dp_sums:
                    s2 = s + v if p == 0 else s - v
                    p2 = 1 - p
                    new_sums.add((s2, p2))
                    new_zero.add((s2, p2))
                    if s2 == k:
                        zero_ok = True

                # also any positive path you had collapses
                for (s, p) in dp_pos:
                    s2 = s + v if p == 0 else s - v
                    p2 = 1 - p
                    new_zero.add((s2, p2))
                    if s2 == k:
                        zero_ok = True

                # and any prior zero-layer carries on too
                for (s, p) in dp_zero:
                    s2 = s + v if p == 0 else s - v
                    p2 = 1 - p
                    new_zero.add((s2, p2))
                    if s2 == k:
                        zero_ok = True

            # 3) Merge updates back in
            dp_sums |= new_sums
            for key, sset in new_pos.items():
                if key in dp_pos:
                    dp_pos[key] |= sset
                else:
                    dp_pos[key] = set(sset)
            dp_zero |= new_zero

        # 4) Final answer
        if best_pos < 0 and not zero_ok:
            return -1
        return max(best_pos, 0)
