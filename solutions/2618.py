class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        
        # 1) Compute initial power for each city via sliding window of width 2r+1
        power = [0] * n
        window = 0
        # initialize window for i = 0: sum stations[0..r]
        for j in range(0, min(n, r + 1)):
            window += stations[j]
        power[0] = window
        
        for i in range(1, n):
            # slide out station at i - r - 1
            if i - r - 1 >= 0:
                window -= stations[i - r - 1]
            # slide in station at i + r
            if i + r < n:
                window += stations[i + r]
            power[i] = window
        
        # 2) Helper to test if we can achieve at least 'target' everywhere
        def can(target):
            diff = [0] * (n + 1)
            add = 0
            remaining = k
            
            for i in range(n):
                add += diff[i]
                curr = power[i] + add
                if curr < target:
                    need = target - curr
                    if need > remaining:
                        return False
                    remaining -= need
                    add += need
                    end = i + 2*r + 1
                    if end < n:
                        diff[end] -= need
            return True
        
        # 3) Binary search answer between min(power) and min(power) + k
        lo = min(power)
        hi = lo + k
        ans = lo
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
