class Solution:
    def minimizeTheDifference(self, mat, target):
        # Compute the maximum possible sum to size our bitmask
        max_sum = sum(max(row) for row in mat)
        # dp is a bitmask where bit s is 1 if sum s is reachable
        dp = 1  # only sum=0 is reachable initially
        
        for row in mat:
            next_dp = 0
            seen = set()
            for v in row:
                if v in seen:  # skip duplicates in the same row
                    continue
                seen.add(v)
                # shift all current sums by v, and OR into next_dp
                next_dp |= dp << v
            dp = next_dp
        
        # Search outward from target for the smallest difference
        limit = max(target, max_sum)
        for d in range(limit + 1):
            lo = target - d
            if lo >= 0 and ((dp >> lo) & 1):
                return d
            hi = target + d
            if hi <= max_sum and ((dp >> hi) & 1):
                return d
        # Should never get here because some sum must be reachable
        return None
