class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def dp(x):
            if x <= 1:
                return x
            if x in memo:
                return memo[x]
            result = min(
                x % 2 + 1 + dp(x // 2),  # eat x % 2 times + 1 (half) + recurse
                x % 3 + 1 + dp(x // 3)   # eat x % 3 times + 1 (2/3) + recurse
            )
            memo[x] = result
            return result

        return dp(n)
