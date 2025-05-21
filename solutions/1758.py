class Solution:
    def canDistribute(self, nums, quantity):
        from collections import Counter
        
        m = len(quantity)
        full = (1<<m) - 1
        
        # 1) Count capacities of each distinct value
        caps = list(Counter(nums).values())
        
        # 2) Precompute demand[mask]
        demand = [0] * (1<<m)
        for mask in range(1, 1<<m):
            # lowest set bit
            lsb = mask & -mask
            i = (lsb.bit_length() - 1)
            prev = mask ^ lsb
            demand[mask] = demand[prev] + quantity[i]
        
        # 3) For each capacity, list valid subsets
        valid = []
        for c in caps:
            lst = []
            for mask in range(1<<m):
                if demand[mask] <= c:
                    lst.append(mask)
            valid.append(lst)
        
        # 4) DP over masks
        dp = [False] * (1<<m)
        dp[0] = True
        
        for lst in valid:
            next_dp = dp[:]  # copy
            for old in range(1<<m):
                if not dp[old]:
                    continue
                free = full ^ old
                # try every subset we can serve with this capacity
                for sub in lst:
                    if sub & old == 0:      # sub â free
                        next_dp[old | sub] = True
            dp = next_dp
        
        return dp[full]
