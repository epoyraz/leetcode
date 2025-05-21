import math
from collections import defaultdict

class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_square_free_part(x):
            res = 1
            d = 2
            while d * d <= x:
                count = 0
                while x % d == 0:
                    x //= d
                    count += 1
                if count % 2 == 1:
                    res *= d
                d += 1
            if x > 1:
                res *= x
            return res

        groups = defaultdict(int)
        for idx, val in enumerate(nums):
            i = idx + 1  # since it's 1-indexed
            key = get_square_free_part(i)
            groups[key] += val

        return max(groups.values())
