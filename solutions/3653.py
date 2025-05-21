class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import math

        n = len(nums)
        # prefix sum
        S = 0
        # min_pref[r] = minimum S_i seen so far with i % k == r
        INF = 10**30
        min_pref = [INF] * k
        min_pref[0] = 0   # S_0 = 0 at index 0 (residue 0)

        ans = -INF
        for j, v in enumerate(nums, start=1):
            S += v
            r = j % k
            # best subarray ending at j whose length divisible by k:
            # S - min_pref[r]
            ans = max(ans, S - min_pref[r])
            # update min prefix for this residue
            min_pref[r] = min(min_pref[r], S)

        return ans
