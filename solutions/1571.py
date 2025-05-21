class Solution(object):
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int
        """
        houses.sort()
        n = len(houses)

        # Precompute the cost to put 1 mailbox for each subarray houses[i..j]
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                median = houses[(i + j) // 2]
                for m in range(i, j + 1):
                    cost[i][j] += abs(houses[m] - median)

        memo = {}

        def dp(i, k):
            if (i, k) in memo:
                return memo[(i, k)]
            if k == 0 and i == n:
                return 0
            if k == 0 or i == n:
                return float('inf')

            res = float('inf')
            for j in range(i, n):
                res = min(res, cost[i][j] + dp(j + 1, k - 1))

            memo[(i, k)] = res
            return res

        result = dp(0, k)
        return result if result != float('inf') else -1
