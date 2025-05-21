import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        H = mountainHeight
        wts = sorted(workerTimes)
        # Upper bound: slowest worker does all H units
        w_max = wts[-1]
        lo, hi = 0, w_max * H * (H + 1) // 2
        ans = hi
        
        while lo <= hi:
            mid = (lo + hi) // 2
            total = 0
            
            for w in wts:
                # If even 1 unit costs more than mid, no contribution
                if w > 2 * mid:
                    break
                
                K = (2 * mid) // w            # floor(2T / w)
                D = 1 + 4 * K
                # integer sqrt via math.sqrt
                s = int(math.sqrt(D))
                # x = floor((sqrt(D)-1)/2)
                x = (s - 1) // 2
                total += x
                if total >= H:
                    break
            
            if total >= H:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans
