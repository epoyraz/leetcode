class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        even = sum(1 for p in position if p % 2 == 0)
        odd = len(position) - even
        return min(even, odd)
