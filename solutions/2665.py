import math

class Solution(object):
    def repairCars(self, ranks, cars):
        # 1) Group mechanics by rank
        freq = [0] * 101
        r_min = float('inf')
        for r in ranks:
            freq[r] += 1
            if r < r_min:
                r_min = r

        # 2) Binaryâsearch the minimal time T
        lo, hi = 0, r_min * (cars ** 2)
        while lo < hi:
            mid = (lo + hi) // 2
            total = 0
            for r in range(1, 101):
                if freq[r]:
                    # max cars one rank-r mechanic can do in 'mid' minutes:
                    # solve r * n^2 <= mid  â  n <= sqrt(mid/r)
                    # use float sqrt then floor
                    done = int(math.sqrt(mid // r))
                    total += freq[r] * done
                    if total >= cars:
                        break
            if total >= cars:
                hi = mid
            else:
                lo = mid + 1
        return lo
