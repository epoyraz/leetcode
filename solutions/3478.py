import math

class Solution:
    # ------------------------------------------------- helpers
    @staticmethod
    def circle_hits_rect(x, y, r, w, h):
        # does the open disk (x-c)Â²+(y-c)Â² < rÂ² meet the open rectangle?
        dx = 0 if 0 < x < w else (0 - x if x <= 0 else x - w)
        dy = 0 if 0 < y < h else (0 - y if y <= 0 else y - h)
        return dx*dx + dy*dy < r*r

    @staticmethod
    def circles_overlap_inside_rect(c1, c2, w, h):
        # does the intersection of two disks enter the rectangleâs interior?
        x1, y1, r1 = c1
        x2, y2, r2 = c2
        dx, dy     = x2 - x1, y2 - y1
        d2         = dx*dx + dy*dy
        rsum       = r1 + r2
        if d2 > rsum*rsum:               # no overlap at all
            return False

        if d2 == 0:                      # concentric
            r_min = min(r1, r2)
            return Solution.circle_hits_rect(x1, y1, r_min, w, h)

        rdiff = abs(r1 - r2)
        if d2 < rdiff*rdiff:             # one disk inside the other
            xc, yc, rc = (x1, y1, r1) if r1 < r2 else (x2, y2, r2)
            return Solution.circle_hits_rect(xc, yc, rc, w, h)

        # proper intersection â compute the two intersection points
        d  = math.sqrt(d2)
        a  = (r1*r1 - r2*r2 + d2) / (2*d)
        h_ = math.sqrt(max(0.0, r1*r1 - a*a))
        xm = x1 + a * dx / d
        ym = y1 + a * dy / d
        rx = -dy * (h_ / d)
        ry =  dx * (h_ / d)
        ix1, iy1 = xm + rx, ym + ry
        ix2, iy2 = xm - rx, ym - ry
        return (0 < ix1 < w and 0 < iy1 < h) or (0 < ix2 < w and 0 < iy2 < h)

    # ------------------------------------------------- main
    def canReachCorner(self, xCorner, yCorner, circles):
        w, h = xCorner, yCorner

        # 0)  either corner covered (or tangent)  â  impossible
        for cx, cy, r in circles:
            if cx*cx + cy*cy <= r*r:
                return False
            dx, dy = cx - w, cy - h
            if dx*dx + dy*dy <= r*r:
                return False

        # 1) keep only disks that intrude the rectangleâs interior
        good = [(x, y, r) for x, y, r in circles
                if self.circle_hits_rect(x, y, r, w, h)]

        n      = len(good)
        parent = list(range(n + 4))          # +4 virtual edge nodes
        LEFT, RIGHT, BOTTOM, TOP = n, n+1, n+2, n+3

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb

        # 2) union disks with edges they touch (tangency counts)
        for i, (x, y, r) in enumerate(good):
            if x - r <= 0 and 0 < y < h:   union(i, LEFT)
            if x + r >= w and 0 < y < h:   union(i, RIGHT)
            if y - r <= 0 and 0 < x < w:   union(i, BOTTOM)
            if y + r >= h and 0 < x < w:   union(i, TOP)

        # 3) union any two disks whose overlap enters the rectangle
        for i in range(n):
            for j in range(i + 1, n):
                if self.circles_overlap_inside_rect(good[i], good[j], w, h):
                    union(i, j)

        # 4) barrier checks
        if find(LEFT)  == find(RIGHT):  return False
        if find(TOP)   == find(BOTTOM): return False
        if find(LEFT)  == find(BOTTOM): return False   # start corner trapped
        if find(RIGHT) == find(TOP):    return False   # goal corner trapped

        return True
