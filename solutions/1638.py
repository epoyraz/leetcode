class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        import math

        def distance(x, y):
            return sum(math.hypot(x - xi, y - yi) for xi, yi in positions)

        # Initialize with centroid
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)

        EPS = 1e-7
        prev = 0
        curr = distance(x, y)

        while abs(curr - prev) > EPS:
            num_x = num_y = denom = 0
            for xi, yi in positions:
                d = math.hypot(x - xi, y - yi)
                if d == 0:  # Avoid division by zero
                    continue
                weight = 1.0 / d
                num_x += xi * weight
                num_y += yi * weight
                denom += weight

            x, y = num_x / denom, num_y / denom
            prev, curr = curr, distance(x, y)

        return curr
