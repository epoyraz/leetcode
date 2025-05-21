class Solution(object):
    def findLength(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        # dp[i][j]: length of longest common suffix of nums1[:i] and nums2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        
        return ans
