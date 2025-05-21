class Solution(object):
    def countWinningSequences(self, s):
        mod = 10**9 + 7
        n = len(s)
        # map F,W,E â 0,1,2
        m = {'F':0,'W':1,'E':2}
        a = [m[ch] for ch in s]

        # f[c][ai] = +1 if c beats ai, -1 if ai beats c, else 0
        f = [[0]*3 for _ in range(3)]
        for c in range(3):
            for ai in range(3):
                d = (c - ai) % 3
                if d == 1:
                    f[c][ai] = 1
                elif d == 2:
                    f[c][ai] = -1

        offset = n
        size = 2*n + 1
        # dp_last[c][offset+diff] = # ways up to previous round,
        # ending with last move c and scoreâdiff = diff
        dp_last = [[0]*size for _ in range(3)]

        # --- initialize for round 0 ---
        for c in range(3):
            delta0 = f[c][a[0]]
            dp_last[c][offset + delta0] = 1

        # current achievable diff range after round 0:
        diff_lo, diff_hi = -1, 1

        # --- process rounds 1..n-1 ---
        for i in range(1, n):
            dp_next = [[0]*size for _ in range(3)]
            ai = a[i]
            # after adding one more round, diff shifts by at most Â±1
            new_lo = max(diff_lo - 1, -n)
            new_hi = min(diff_hi + 1,  n)

            # transition
            for last in range(3):
                row = dp_last[last]
                for diff in range(diff_lo, diff_hi+1):
                    ways = row[offset + diff]
                    if not ways:
                        continue
                    # Bobâs next move c â  last
                    for c in range(3):
                        if c == last:
                            continue
                        nd = diff + f[c][ai]
                        dp_next[c][offset + nd] = (dp_next[c][offset + nd] + ways) % mod

            dp_last = dp_next
            diff_lo, diff_hi = new_lo, new_hi

        # --- sum all ways with final diff > 0 ---
        ans = 0
        for last in range(3):
            row = dp_last[last]
            for d in range(1, n+1):
                ans = (ans + row[offset + d]) % mod

        return ans
