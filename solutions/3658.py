import heapq

class Solution(object):
    def minDifference(self, nums):
        """
        Return the smallest k such that all â1 positions can be replaced with two
        positive integers x and y so that every adjacent pair differs by â¤ k.
        """
        INF = 4 * 10 ** 9
        n   = len(nums)

        if all(v == -1 for v in nums):
            return 0                               # everything can be 1

        # ------------------------------------------------------------------ #
        # Things that never change while we binary-search on k
        # ------------------------------------------------------------------ #
        fixed_pairs = [abs(nums[i] - nums[i + 1])
                       for i in range(n - 1)
                       if nums[i] != -1 and nums[i + 1] != -1]

        # helper: build intervals [L,R] for every â-1â slot, or return None if impossible
        def build_intervals(k):
            L, R, idx_of = [], [], {}
            for i, v in enumerate(nums):
                if v != -1:
                    continue
                lo, hi = 1, INF
                if i and nums[i - 1] != -1:
                    lo = max(lo, nums[i - 1] - k)
                    hi = min(hi, nums[i - 1] + k)
                if i + 1 < n and nums[i + 1] != -1:
                    lo = max(lo, nums[i + 1] - k)
                    hi = min(hi, nums[i + 1] + k)
                if lo > hi:
                    return None
                idx_of[i] = len(L)
                L.append(lo)
                R.append(hi)
            return L, R, idx_of

        # ------------------------------------------------------------------ #
        # 1) âno-mixâ feasibility: every consecutive block of -1 takes ONE value
        # ------------------------------------------------------------------ #
        def no_mix_feasible(k, L, R, idx_of):
            blocks, i = [], 0
            while i < n:
                if nums[i] != -1:
                    i += 1
                    continue
                lo, hi, j = 1, INF, i
                while j < n and nums[j] == -1:
                    p = idx_of[j]
                    lo = max(lo, L[p])
                    hi = min(hi, R[p])
                    j += 1
                if lo > hi:                        # whole block impossible
                    return False
                blocks.append((lo, hi))
                i = j

            if not blocks:                         # no â-1â at all
                return True

            # classic âstab all intervals with â¤ 2 pointsâ greedy
            blocks.sort(key=lambda x: x[1])
            used, ptr = 0, 0
            while ptr < len(blocks) and used < 2:
                p = blocks[ptr][1]                 # take right end
                used += 1
                ptr += 1
                while ptr < len(blocks) and blocks[ptr][0] <= p <= blocks[ptr][1]:
                    ptr += 1
            return ptr == len(blocks)

        # ------------------------------------------------------------------ #
        # 2) âmixâ feasibility: we may have x next to y (needs |x-y| â¤ k)
        # ------------------------------------------------------------------ #
        def mix_feasible(k, L, R, idx_of):
            m = len(L)
            if m == 0:
                return True                        # nothing to fill

            # global intersection â if non-empty weâre done (x fills everything)
            gL = max(L); gR = min(R)
            if gL <= gR:
                return True

            # ---- sort by L and by R once ----------------------------------
            order_L = sorted(range(m), key=lambda i: L[i])
            L_sorted  = [L[i] for i in order_L]
            R_by_L    = [R[i] for i in order_L]

            suf_max_L = [0] * m
            suf_min_R = [0] * m
            suf_max_L[-1] = L_sorted[-1]
            suf_min_R[-1] = R_by_L[-1]
            for i in range(m - 2, -1, -1):
                suf_max_L[i] = max(suf_max_L[i + 1], L_sorted[i])
                suf_min_R[i] = min(suf_min_R[i + 1], R_by_L[i])

            order_R = sorted(range(m), key=lambda i: R[i])
            R_sorted   = [R[i] for i in order_R]
            L_by_R     = [L[i] for i in order_R]

            pre_max_L = [0] * m
            pre_max_L[0] = L_by_R[0]
            for i in range(1, m):
                pre_max_L[i] = max(pre_max_L[i - 1], L_by_R[i])

            # ---- build âmixing activeâ events (+1 at start, -1 at end+1) ---
            mix_events = []
            for i in range(n - 1):
                if nums[i] == -1 and nums[i + 1] == -1:      # â fixed line
                    a = idx_of[i]
                    b = idx_of[i + 1]
                    L1, R1 = L[a], R[a]
                    L2, R2 = L[b], R[b]

                    lo_seg = (min(L1, L2), max(L1, L2) - 1)
                    if lo_seg[0] <= lo_seg[1]:
                        mix_events.append((lo_seg[0], 1))
                        mix_events.append((lo_seg[1] + 1, -1))

                    hi_seg = (min(R1, R2) + 1, max(R1, R2))
                    if hi_seg[0] <= hi_seg[1]:
                        mix_events.append((hi_seg[0], 1))
                        mix_events.append((hi_seg[1] + 1, -1))
            mix_events.sort()

            # ---- collect sweep coordinates ---------------------------------
            coords = {1}
            for v in L:
                coords.add(v)
            for v in R:
                if v < INF:
                    coords.add(v + 1)
            for c, _ in mix_events:
                coords.add(c)
            coords = sorted(coords)

            pL = pR = 0
            mix_ptr = mix_cnt = 0
            len_L = len(L_sorted)
            len_R = len(R_sorted)

            for ci in range(len(coords) - 1):
                x_min = coords[ci]
                x_max = coords[ci + 1] - 1

                # advance pointers so that:
                #   L_sorted[:pL]  â L â¤ x_min
                #   R_sorted[:pR]  â R < x_min
                while pL < len_L and L_sorted[pL] <= x_min:
                    pL += 1
                while pR < len_R and R_sorted[pR] < x_min:
                    pR += 1

                # apply every mix-event that starts exactly at x_min
                while mix_ptr < len(mix_events) and mix_events[mix_ptr][0] == x_min:
                    mix_cnt += mix_events[mix_ptr][1]
                    mix_ptr += 1

                # L*  = max(L of L> x)  vs  max(L of R< x)
                g1_max = suf_max_L[pL] if pL < len_L else -1
                g2_max = pre_max_L[pR - 1] if pR else -1
                L_star = max(g1_max, g2_max)

                # R*  = min(R of L> x)  vs  min(R of R< x)
                g1_min = suf_min_R[pL] if pL < len_L else INF
                g2_min = R_sorted[0]    if pR else INF
                R_star = min(g1_min, g2_min)

                if L_star > R_star:          # intersection empty â impossible here
                    continue

                if mix_cnt == 0:             # no xây adjacency â feasible
                    return True

                # need distance(x, [L*,R*]) â¤ k for *some* x in [x_min,x_max]
                if x_max < L_star:
                    d = L_star - x_max
                elif x_min > R_star:
                    d = x_min - R_star
                else:
                    d = 0
                if d <= k:
                    return True

            return False                     # sweep finished, no luck

        # ------------------------------------------------------------------ #
        # Feasibility wrapper for a given k
        # ------------------------------------------------------------------ #
        def feasible(k):
            if fixed_pairs and max(fixed_pairs) > k:
                return False

            built = build_intervals(k)
            if built is None:
                return False
            L, R, idx_of = built

            if no_mix_feasible(k, L, R, idx_of):
                return True
            return mix_feasible(k, L, R, idx_of)

        # ------------------------------------------------------------------ #
        # Binary search on k
        # ------------------------------------------------------------------ #
        lo, hi, ans = 0, 2 * 10 ** 9, 2 * 10 ** 9
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans, hi = mid, mid - 1
            else:
                lo = mid + 1
        return ans
