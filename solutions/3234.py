class Solution(object):
    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute a^b mod 10
            x = pow(a, b, 10)
            # Then compute x^c mod m
            if pow(x, c, m) == target:
                res.append(i)
        return res
