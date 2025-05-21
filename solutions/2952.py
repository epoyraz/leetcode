class Solution(object):
    def minimumTime(self, nums1, nums2, x):
        n = len(nums1)
        total1 = sum(nums1)
        total2 = sum(nums2)
        if total1 <= x:
            return 0

        pairs = sorted(zip(nums2, nums1))          # sort by nums2 ascending
        neg_inf = -10**18
        dp = [neg_inf] * (n + 1)
        dp[0] = 0

        for b, a in pairs:                         # b = nums2, a = nums1
            for j in range(n - 1, -1, -1):
                if dp[j] == neg_inf:
                    continue
                val = dp[j] + a + (j + 1) * b
                if val > dp[j + 1]:
                    dp[j + 1] = val

        for t in range(1, n + 1):
            if total1 + t * total2 - dp[t] <= x:
                return t
        return -1
