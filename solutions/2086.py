class Solution(object):
    def countSpecialSubsequences(self, nums):
        MOD = 10**9 + 7
        dp0 = dp1 = dp2 = 0
        for x in nums:
            if x == 0:
                dp0 = (dp0 * 2 + 1) % MOD
            elif x == 1:
                dp1 = (dp1 * 2 + dp0) % MOD
            else:  # x == 2
                dp2 = (dp2 * 2 + dp1) % MOD
        return dp2
