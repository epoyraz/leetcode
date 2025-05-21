class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        d1 = abs(x - z)
        d2 = abs(y - z)
        if d1 < d2:
            return 1
        elif d2 < d1:
            return 2
        else:
            return 0
