class Solution(object):
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        """
        :type n: int
        :type k: int
        :type budget: int
        :type composition: List[List[int]]
        :type stock: List[int]
        :type cost: List[int]
        :rtype: int
        """

        def can_make(x):
            for machine in composition:
                total_cost = 0
                for j in range(n):
                    required = machine[j] * x
                    if required > stock[j]:
                        total_cost += (required - stock[j]) * cost[j]
                if total_cost <= budget:
                    return True
            return False

        # Binary search on number of alloys
        left, right = 0, 10**9
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if can_make(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
