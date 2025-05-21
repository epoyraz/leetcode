from bisect import bisect_left, bisect_right

class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        # total available single-step reductions
        K = k1 + k2
        n = len(nums1)
        
        # compute and sort absolute differences
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        diffs.sort()
        
        # build prefix sums of diffs and diffs^2
        pref = [0] * (n + 1)
        pref_sq = [0] * (n + 1)
        for i, d in enumerate(diffs):
            pref[i+1] = pref[i] + d
            pref_sq[i+1] = pref_sq[i] + d * d
        
        # cost(T): how many single-step reductions needed
        # to bring every diff down to at most T
        def cost(T):
            idx = bisect_right(diffs, T)
            # sum(diffs[idx:]) - (n - idx) * T
            return (pref[n] - pref[idx]) - (n - idx) * T
        
        # binary search the smallest T so cost(T) <= K
        low, high = 0, diffs[-1]
        while low < high:
            mid = (low + high) // 2
            if cost(mid) <= K:
                high = mid
            else:
                low = mid + 1
        T = low
        
        # if T == 0, we can zero out all differences
        if T == 0:
            return 0
        
        # how many operations used to bring >T down to T
        used = cost(T)
        leftover = K - used
        
        # count how many diffs are exactly T (after leveling)
        idx_ge = bisect_left(diffs, T)
        C = n - idx_ge
        
        # sum of squares for those originally below T
        sum_below = pref_sq[idx_ge]
        
        # of the C entries at T, we use 'leftover' of them to reduce to T-1
        L = leftover  # guaranteed L < C
        
        # total sum of squares
        total = sum_below
        total += L * (T-1) * (T-1)
        total += (C - L) * T * T
        
        return total
