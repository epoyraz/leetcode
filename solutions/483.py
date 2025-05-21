import math

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        num = int(n)
        max_m = int(math.log(num + 1, 2))  # max possible length of all-1's

        for m in range(max_m, 1, -1):
            k = int(num ** (1.0 / (m - 1)))
            if k < 2:
                continue
            # Check if 1 + k + k^2 + ... + k^(m-1) == num
            total = (k ** m - 1) // (k - 1)
            if total == num:
                return str(k)

        return str(num - 1)
