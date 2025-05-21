class Solution(object):
    def minCost(self, arr, brr, k):
        """
        :type arr: List[int]
        :type brr: List[int]
        :type k: int
        :rtype: int
        """
        # 1) Cost if we never pay k: just adjust in place
        cost_no_perm = sum(abs(a - b) for a, b in zip(arr, brr))
        
        # 2) Cost if we do one free-form rearrangement (cost k)
        #    + then adjust each element.
        #    The best rearrangement for sum |a-b| is to match
        #    sorted(arr) with sorted(brr).
        sa = sorted(arr)
        sb = sorted(brr)
        matching_cost = sum(abs(a - b) for a, b in zip(sa, sb))
        cost_with_perm = k + matching_cost
        
        return min(cost_no_perm, cost_with_perm)
