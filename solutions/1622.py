from collections import deque

class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        dq = deque()  # stores (yi - xi, xi)
        res = float('-inf')

        for xj, yj in points:
            # Remove points where xj - xi > k
            while dq and xj - dq[0][1] > k:
                dq.popleft()

            # Use the best candidate in deque
            if dq:
                res = max(res, yj + xj + dq[0][0])  # dq[0][0] = yi - xi

            # Maintain deque: remove back if worse than current
            while dq and dq[-1][0] <= yj - xj:
                dq.pop()

            dq.append((yj - xj, xj))

        return res
