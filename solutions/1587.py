from itertools import combinations

class Solution(object):
    def minNumberOfSemesters(self, n, relations, k):
        """
        :type n: int
        :type relations: List[List[int]]
        :type k: int
        :rtype: int
        """
        prereq = [0] * n
        for prev, nxt in relations:
            prereq[nxt - 1] |= 1 << (prev - 1)

        memo = {}

        def dp(mask):
            if mask == (1 << n) - 1:
                return 0  # All courses taken

            if mask in memo:
                return memo[mask]

            available = []
            for i in range(n):
                if (mask >> i) & 1 == 0 and (prereq[i] & mask) == prereq[i]:
                    available.append(i)

            res = float('inf')

            for subset in combinations(available, min(k, len(available))):
                new_mask = mask
                for course in subset:
                    new_mask |= 1 << course
                res = min(res, 1 + dp(new_mask))

            memo[mask] = res
            return res

        return dp(0)
