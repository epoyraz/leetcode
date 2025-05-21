class Solution:
    def minTaps(self, n, ranges):
        # Build maxReach: for each position i, the farthest right endpoint
        # of any interval starting at i
        maxReach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            maxReach[left] = max(maxReach[left], right)
        
        taps = 0
        curr_end = 0
        next_end = 0
        i = 0
        
        # Greedy jump through [0..n]
        while curr_end < n:
            # Extend coverage as far as possible from any start <= curr_end
            while i <= curr_end:
                next_end = max(next_end, maxReach[i])
                i += 1
            # If we cannot extend beyond curr_end, fail
            if next_end == curr_end:
                return -1
            # Use one more tap to extend coverage
            taps += 1
            curr_end = next_end
        
        return taps
