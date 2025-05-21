class Solution:
    def countPartitions(self, nums, k):
        mod = 10**9 + 7
        n = len(nums)
        total = sum(nums)
        
        # If total < 2k, impossible for both groups to reach k
        if total < 2 * k:
            return 0
        # If k == 0, every partition is valid
        if k == 0:
            return pow(2, n, mod)
        
        # Only "small" candies (value < k) can appear in a subset summing to < k.
        small = [v for v in nums if v < k]
        
        # dp[s] = number of subsets of `small` that sum to exactly s (for 0 <= s < k)
        dp = [0] * k
        dp[0] = 1
        
        for v in small:
            # update in reverse to avoid reuse
            for s in range(k - 1, v - 1, -1):
                dp[s] = (dp[s] + dp[s - v]) % mod
        
        # C = number of subsets of small with sum < k
        C = sum(dp) % mod
        
        total_partitions = pow(2, n, mod)
        # Subtract partitions where group A sum<k (C) or group B sum<k (C)
        # (they are disjoint when total >= 2k)
        ans = (total_partitions - 2 * C) % mod
        return ans
