class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        suffix = int(s)
        L = len(s)
        base = 10 ** L
        if finish < suffix:
            return 0
        # compute t range so that t*base + suffix â [start, finish]
        t_min = 0
        if start > suffix:
            t_min = (start - suffix + base - 1) // base
        t_max = (finish - suffix) // base
        if t_max < t_min:
            return 0

        def count(N):
            if N < 0:
                return 0
            digs = list(map(int, str(N)))
            n = len(digs)
            memo = {}
            def dp(pos, tight):
                if pos == n:
                    return 1
                key = (pos, tight)
                if key in memo:
                    return memo[key]
                if tight:
                    up = min(digs[pos], limit)
                else:
                    up = limit
                total = 0
                for d in range(up + 1):
                    total += dp(pos + 1, tight and d == digs[pos])
                memo[key] = total
                return total
            return dp(0, True)

        return count(t_max) - count(t_min - 1)
