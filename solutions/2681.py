class Solution:
    def putMarbles(self, weights, k):
        n = len(weights)
        if k == 1:
            return 0
        
        # Compute boundary sums for possible cut positions
        boundary_sums = [weights[i-1] + weights[i] for i in range(1, n)]
        boundary_sums.sort()
        
        # Sum of smallest (k-1) and largest (k-1)
        small_sum = sum(boundary_sums[:k-1])
        large_sum = sum(boundary_sums[-(k-1):])
        
        return large_sum - small_sum
