class Solution(object):
    def findMinimumTime(self, strength, k):
        """
        :type strength: List[int]
        :type k: int
        :rtype: int
        """
        n = len(strength)
        ALL = (1<<n) - 1
        INF = 10**18

        # dp[mask] = min time to break exactly the locks in 'mask'
        dp = [INF] * (1<<n)
        dp[0] = 0

        for mask in range(1<<n):
            base = dp[mask]
            if base == INF:
                continue

            # count how many locks already broken
            c = bin(mask).count('1')
            x = 1 + c * k

            for i in range(n):
                if not (mask & (1<<i)):
                    # time to break lock i at factor x
                    t = (strength[i] + x - 1) // x
                    new_mask = mask | (1<<i)
                    if base + t < dp[new_mask]:
                        dp[new_mask] = base + t

        return dp[ALL]
