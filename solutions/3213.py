from bisect import bisect_left

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        M = max(nums)
        # Positions where the global maximum M occurs
        P = [i for i, v in enumerate(nums) if v == M]
        t = len(P)
        if t < k:
            return 0
        
        ans = 0
        # For each starting index L, find the earliest occurrence of M at or after L
        # that will serve as the k-th occurrence in the subarray.
        for L in range(n):
            j = bisect_left(P, L)
            # If there are at least k occurrences from j onward:
            if j + k - 1 < t:
                # the subarray must end at R >= P[j+k-1]
                # so we get (n - P[j+k-1]) choices for R
                ans += n - P[j + k - 1]
        return ans
