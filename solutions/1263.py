class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        memo = {}

        def dp(dice, total):
            if dice == 0:
                return 1 if total == 0 else 0
            if total < 0:
                return 0
            if (dice, total) in memo:
                return memo[(dice, total)]

            res = 0
            for face in range(1, k + 1):
                res = (res + dp(dice - 1, total - face)) % MOD

            memo[(dice, total)] = res
            return res

        return dp(n, target)
