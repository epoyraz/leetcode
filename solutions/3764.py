class Solution(object):
    def maxSum(self, grid, limits, k):
        """
        :type grid: List[List[int]]
        :type limits: List[int]
        :type k: int
        :rtype: int
        """
        cand = []
        for row, lim in zip(grid, limits):
            # sort this row descending
            row.sort(reverse=True)
            # take up to `lim` largest pizzas
            cand.extend(row[:lim])
        # pick the k largest across all rows
        cand.sort(reverse=True)
        # sum up the top k (or all, if fewer than k)
        return sum(cand[:k])
