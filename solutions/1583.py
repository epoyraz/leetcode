class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        INF = float('inf')
        cache = {}

        def dp(i, prev_color, neighborhoods):
            if neighborhoods > target:
                return INF
            if i == m:
                return 0 if neighborhoods == target else INF

            key = (i, prev_color, neighborhoods)
            if key in cache:
                return cache[key]

            if houses[i] != 0:
                new_neigh = neighborhoods + (1 if houses[i] != prev_color else 0)
                res = dp(i + 1, houses[i], new_neigh)
            else:
                res = INF
                for color in range(1, n + 1):
                    new_neigh = neighborhoods + (1 if color != prev_color else 0)
                    paint_cost = cost[i][color - 1]
                    total = paint_cost + dp(i + 1, color, new_neigh)
                    res = min(res, total)

            cache[key] = res
            return res

        result = dp(0, 0, 0)
        return -1 if result == INF else result
