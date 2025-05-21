class Solution:
    def minSpeedOnTime(self, dist, hour):
        # parse hour (float with <=2 decimals) into numerator/denominator
        h = str(hour)
        if '.' in h:
            a, b = h.split('.')
            denom = 10 ** len(b)
            numer = int(a) * denom + int(b)
        else:
            numer = int(h)
            denom = 1

        n = len(dist)
        # if even the (n-1) mandatory integer-hour waits exceed hour, impossible
        if numer < denom * (n - 1):
            return -1

        # check feasibility at speed v using integer arithmetic only
        def ok(v):
            # S1 = sum of ceil(dist[i]/v) for i in [0..n-2]
            S1 = 0
            for d in dist[:-1]:
                S1 += (d + v - 1) // v
                # early exit if already too many whole hours
                if S1 * denom > numer:
                    return False
            # total_time * denom <= hour * denom
            # total_time = S1 + dist[-1]/v
            # â (S1 * v + dist[-1]) * denom <= numer * v
            left = (S1 * v + dist[-1]) * denom
            right = numer * v
            return left <= right

        # if max speed still fails, impossible
        MAX = 10**7
        if not ok(MAX):
            return -1

        lo, hi, ans = 1, MAX, MAX
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
