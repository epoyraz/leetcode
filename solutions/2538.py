class Solution(object):
    def minCost(self, nums, cost):
        # Pair and sort by nums
        pairs = sorted(zip(nums, cost))
        total_cost = sum(cost for _, cost in pairs)
        # Find weighted median target value x
        cum = 0
        half = (total_cost + 1) // 2
        for val, c in pairs:
            cum += c
            if cum >= half:
                x = val
                break
        
        # Compute total cost at x
        ans = 0
        for v, c in pairs:
            ans += abs(v - x) * c
        return ans
