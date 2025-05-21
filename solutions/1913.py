from collections import Counter

class Solution(object):
    def minChanges(self, nums, k):
        MAXX = 1 << 10  # Since nums[i] < 2^10
        dp = [float('inf')] * MAXX
        dp[0] = 0

        for i in range(k):
            count = Counter()
            total = 0
            for j in range(i, len(nums), k):
                count[nums[j]] += 1
                total += 1

            min_dp = min(dp)
            ndp = [min_dp + total] * MAXX

            for mask in range(MAXX):
                for x in count:
                    ndp[mask] = min(ndp[mask], dp[mask ^ x] + total - count[x])

            dp = ndp

        return dp[0]
