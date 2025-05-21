import math

class Solution(object):
    def numPoints(self, darts, r):
        n = len(darts)
        if n == 0:
            return 0
        res = 1
        r2 = r * r
        for i in range(n):
            x1, y1 = darts[i]
            # Center at dart i
            cnt = 0
            for xk, yk in darts:
                if (xk - x1) ** 2 + (yk - y1) ** 2 <= r2:
                    cnt += 1
            res = max(res, cnt)
            # Circles through dart i and dart j
            for j in range(i + 1, n):
                x2, y2 = darts[j]
                dx, dy = x2 - x1, y2 - y1
                d2 = dx*dx + dy*dy
                if d2 > 4 * r2:
                    continue
                d = math.sqrt(d2)
                # midpoint
                mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
                # distance from midpoint to centers
                h = math.sqrt(r2 - (d/2.0)**2)
                # unit perpendicular
                ux, uy = -dy / d, dx / d
                # two possible centers
                for sign in (1, -1):
                    cx = mx + sign * h * ux
                    cy = my + sign * h * uy
                    cnt = 0
                    for xk, yk in darts:
                        if (xk - cx) ** 2 + (yk - cy) ** 2 <= r2 + 1e-9:
                            cnt += 1
                    res = max(res, cnt)
        return res
