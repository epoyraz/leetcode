class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        concatenated = str(n) + str(n * 2) + str(n * 3)
        if '0' in concatenated or len(concatenated) != 9:
            return False
        return sorted(concatenated) == list('123456789')
