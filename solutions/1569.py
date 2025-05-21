class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        # dp[i][j] = max dot product using nums1[:i] and nums2[:j]
        NEG_INF = -10**18
        dp = [[NEG_INF] * (n+1) for _ in range(m+1)]
        ans = NEG_INF
        for i in range(1, m+1):
            for j in range(1, n+1):
                prod = nums1[i-1] * nums2[j-1]
                dp[i][j] = max(
                    dp[i-1][j],          # skip nums1[i-1]
                    dp[i][j-1],          # skip nums2[j-1]
                    dp[i-1][j-1] + prod, # take both and extend
                    prod                 # start new subsequence here
                )
                ans = max(ans, dp[i][j])
        return ans
