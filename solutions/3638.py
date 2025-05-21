class Solution(object):
    def makeStringGood(self, s):
        # 1) histogram -------------------------------------------------------
        f = [0] * 26
        for ch in s:
            f[ord(ch) - 97] += 1
        M = max(f)                       # largest bucket,  â¤ n

        INF  = 10 ** 9
        best = INF

        # 2) try every target multiplicity k = 1 â¦ M ------------------------
        for k in xrange(1, M + 1):

            # dp[inc_prev][has_kept_any]
            dp = [[INF, INF], [INF, INF]]
            dp[0][0] = f[0]              # delete bucket 'a'
            dp[1][1] = abs(f[0] - k)     # keep bucket 'a'

            # walk through 'b' â¦ 'z'
            for i in xrange(1, 26):
                ndp = [[INF, INF], [INF, INF]]

                for inc_prev in (0, 1):
                    for has in (0, 1):
                        cur = dp[inc_prev][has]
                        if cur >= INF:
                            continue

                        surplus_prev = f[i-1] if inc_prev == 0 \
                                       else max(0, f[i-1] - k)

                        for inc in (0, 1):
                            cost_now = f[i] if inc == 0 \
                                       else abs(f[i] - k)
                            deficit  = 0 if inc == 0 \
                                       else max(0, k - f[i])

                            benefit  = min(surplus_prev, deficit)  # use change
                            new_has  = has or inc

                            cand = cur + cost_now - benefit
                            if cand < ndp[inc][new_has]:
                                ndp[inc][new_has] = cand

                dp = ndp

            best = min(best, dp[0][1], dp[1][1])     # must keep â¥ 1 bucket

        return best
