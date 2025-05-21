class Solution:
    def maxSubarrays(self, nums):
        n = len(nums)
        INF = 10**18
        # f[i]: min total score for first i elements
        # g[i]: max #subarrays achieving f[i]
        f = [INF] * (n + 1)
        g = [0] * (n + 1)
        f[0] = 0
        
        # prev maps AND-value -> (best_prefix_sum, best_prefix_segments)
        prev = {}
        
        for i, x in enumerate(nums):
            new = {}
            # Extend every subarray ending at i-1
            for v, (fj, gj) in prev.items():
                v_new = v & x
                old = new.get(v_new)
                if old is None or fj < old[0] or (fj == old[0] and gj > old[1]):
                    new[v_new] = (fj, gj)
            # Single-element subarray [i..i]
            old = new.get(x)
            if old is None or f[i] < old[0] or (f[i] == old[0] and g[i] > old[1]):
                new[x] = (f[i], g[i])
            # Choose the best split ending at i
            best_sum = INF
            best_segs = 0
            for v_new, (fj, gj) in new.items():
                total = fj + v_new
                segs = gj + 1
                if total < best_sum or (total == best_sum and segs > best_segs):
                    best_sum = total
                    best_segs = segs
            f[i + 1] = best_sum
            g[i + 1] = best_segs
            prev = new
        
        return g[n]