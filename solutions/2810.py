class Solution:
    def minCost(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums)
        # best_costs[t] = min cost to collect type t using up to r rotations
        best_costs = nums[:]  # for r = 0, window size = 1
        total = sum(best_costs)
        ans = total  # r = 0, rotation cost = 0
        
        # try r = 1 to n-1 rotations
        for r in range(1, n):
            # include the cost of the newly reachable index for each t:
            # index = (t - r) mod n
            for t in range(n):
                candidate = nums[(t - r) % n]
                if candidate < best_costs[t]:
                    best_costs[t] = candidate
            total = sum(best_costs)
            cost = total + r * x
            if cost < ans:
                ans = cost
        
        return ans
