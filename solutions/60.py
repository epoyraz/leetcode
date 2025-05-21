class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial

        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1
        res = ""

        for i in range(n, 0, -1):
            f = factorial(i - 1)
            index = k // f
            res += numbers[index]
            numbers.pop(index)
            k %= f

        return res
