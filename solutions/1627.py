class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        max_left = max(left) if left else 0
        max_right = max([n - r for r in right]) if right else 0
        return max(max_left, max_right)
