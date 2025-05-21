class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        res = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            res += count[key]
            count[key] += 1

        return res
