class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        import math

        n = len(s)
        # 1) Runâlength encode s into runs[]
        runs = []          # list of tuples (char, start, end, length)
        run_id = [0]*n     # run_id[i] = index in runs[] containing s[i]
        i = 0
        rid = 0
        while i < n:
            j = i
            while j+1 < n and s[j+1] == s[i]:
                j += 1
            runs.append((s[i], i, j, j - i + 1))
            for k in range(i, j+1):
                run_id[k] = rid
            rid += 1
            i = j + 1
        R = rid

        # Unpack runs into parallel arrays
        run_char  = [runs[k][0] for k in range(R)]
        run_start = [runs[k][1] for k in range(R)]
        run_end   = [runs[k][2] for k in range(R)]
        run_len   = [runs[k][3] for k in range(R)]

        INF = 10**15
        # 2a) Build array for minâoneârunÂ­length RMQ (INF on zeroâruns)
        arr_one_min = [INF]*R
        for k in range(1, R-1):
            if run_char[k] == '1':
                arr_one_min[k] = run_len[k]

        # 2b) Build array for maxâzeroârun RMQ
        arr_zero_max = [0]*R
        for k in range(R):
            if run_char[k] == '0':
                arr_zero_max[k] = run_len[k]

        # 2c) Build array for mergingâzeros RMQ:
        #    around each oneârun k: run_len[k-1] + run_len[k+1]
        arr_merge_max = [0]*R
        for k in range(1, R-1):
            if run_char[k] == '1':
                arr_merge_max[k] = run_len[k-1] + run_len[k+1]

        # --- Sparse table boilerplate ---------------------
        # Precompute logs
        log = [0]*(R+1)
        for x in range(2, R+1):
            log[x] = log[x//2] + 1
        K = log[R] + 1

        def build_rmq_max(arr):
            st = [arr[:]]
            j = 1
            while (1<<j) <= R:
                prev = st[j-1]
                cur = [max(prev[i], prev[i + (1<<(j-1))]) 
                       for i in range(R - (1<<j) + 1)]
                st.append(cur)
                j += 1
            return st

        def build_rmq_min(arr):
            st = [arr[:]]
            j = 1
            while (1<<j) <= R:
                prev = st[j-1]
                cur = [min(prev[i], prev[i + (1<<(j-1))]) 
                       for i in range(R - (1<<j) + 1)]
                st.append(cur)
                j += 1
            return st

        def rmq_max(st, L, R_):
            """max over arr[L..R_]"""
            j = log[R_ - L + 1]
            row = st[j]
            return max(row[L], row[R_ - (1<<j) + 1])

        def rmq_min(st, L, R_):
            """min over arr[L..R_]"""
            j = log[R_ - L + 1]
            row = st[j]
            return min(row[L], row[R_ - (1<<j) + 1])

        st_zero_max = build_rmq_max(arr_zero_max)
        st_one_min  = build_rmq_min(arr_one_min)
        st_merge_max= build_rmq_max(arr_merge_max)

        total_ones = s.count('1')
        ans = []

        # 3) Answer each query in O(1) RMQs + O(1) edge logic
        for l, r in queries:
            il = run_id[l]
            ir = run_id[r]

            # 3a) longest zeroâblock in [l,r]:
            left_z = 0
            if s[l] == '0':
                left_z = min(run_end[il], r) - l + 1
            right_z = 0
            if s[r] == '0':
                right_z = r - max(run_start[ir], l) + 1

            mid_z = 0
            if il+1 <= ir-1:
                mid_z = rmq_max(st_zero_max, il+1, ir-1)

            Z_max = max(left_z, right_z, mid_z)

            # 3b) find all oneâruns fully inside (l,r):
            jl = max(il+1, 1)
            jr = min(ir-1, R-2)
            if jl > jr:
                # no oneârun we can flip
                ans.append(total_ones)
                continue

            L1_min = rmq_min(st_one_min, jl, jr)
            if L1_min >= INF:
                # no valid oneârun strictly inside
                ans.append(total_ones)
                continue

            gain1 = Z_max - L1_min  # using existing zeroâblock

            # 3c) best merge from flipping oneârun â zeros
            best_merge = 0
            # interior: j in [jl+1, jr-1]
            mL = jl+1
            mR = jr-1
            if mL <= mR:
                best_merge = rmq_max(st_merge_max, mL, mR)

            # boundary j = jl
            j = jl
            if run_char[j] == '1':
                left_part  = max(0, run_end[j-1] - l + 1)
                right_part = max(0, min(run_end[j+1], r) - run_start[j+1] + 1)
                best_merge = max(best_merge, left_part + right_part)

            # boundary j = jr (if distinct)
            if jr != jl:
                j = jr
                if run_char[j] == '1':
                    left_part  = max(0, min(run_end[j-1], r) - max(run_start[j-1], l) + 1)
                    right_part = max(0, r - run_start[j+1] + 1)
                    best_merge = max(best_merge, left_part + right_part)

            gain2 = best_merge
            gain  = max(0, gain1, gain2)
            ans.append(total_ones + gain)

        return ans
