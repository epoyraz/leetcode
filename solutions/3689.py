import bisect
from collections import defaultdict

class Fenwick:
    def __init__(self, n):
        # 1-indexed Fenwick tree over [0..n-1]
        self.n = n
        self.fw = [0]*(n+1)
    def add(self, i, v):
        # add v at index i (0-based)
        i += 1
        while i <= self.n:
            self.fw[i] += v
            i += i & -i
    def sum(self, i):
        # sum of [0..i] (0-based)
        i += 1
        s = 0
        while i>0:
            s += self.fw[i]
            i -= i & -i
        return s
    def range_sum(self, l, r):
        if l>r:
            return 0
        return self.sum(r) - (self.sum(l-1) if l>0 else 0)

class Solution(object):
    def maxRectangleArea(self, xCoord, yCoord):
        points = list(zip(xCoord, yCoord))
        n = len(points)

        # 1) Build H and collect horizontal edges
        H = defaultdict(list)
        V = defaultdict(list)
        for x,y in points:
            H[y].append(x)
            V[x].append(y)
        for y in H: H[y].sort()
        for x in V: V[x].sort()

        by_edge = defaultdict(list)  # keyed by (x1,x2) -> list of y's
        for y, xs in H.items():
            for i in range(len(xs)-1):
                x1, x2 = xs[i], xs[i+1]
                by_edge[(x1,x2)].append(y)
        for key in by_edge:
            by_edge[key].sort()

        # 2) Gather candidate rectangles:
        #    only consecutive y's for each (x1,x2), and vertical edges must be clean
        def are_adj(lst, a, b):
            # check a,b are consecutive in sorted list lst
            ia = bisect.bisect_left(lst, a)
            ib = bisect.bisect_left(lst, b)
            return abs(ia-ib) == 1

        cands = []  # (x1,x2,y1,y2,area)
        for (x1,x2), ylist in by_edge.items():
            for i in range(len(ylist)-1):
                y1 = ylist[i]
                y2 = ylist[i+1]
                # must be adjacent vertically too
                if not are_adj(V[x1], y1, y2): continue
                if not are_adj(V[x2], y1, y2): continue
                area = (x2-x1)*(y2-y1)
                if area>0:
                    cands.append((x1, x2, y1, y2, area))

        if not cands:
            return -1

        # 3) Prepare sweep: events to test interior emptiness
        # Each cand idx produces two events:
        #   at x1+1 with sign -1, at x2 with sign +1
        events = []  # (x_evt, y1, y2, sign, cand_idx)
        for idx, (x1,x2,y1,y2,_) in enumerate(cands):
            events.append((x1+1, y1, y2, -1, idx))
            events.append((x2,   y1, y2, +1, idx))
        events.sort(key=lambda e: e[0])

        # 4) Fenwick over all y's
        all_y = sorted({y for _,y in points})
        fenw = Fenwick(len(all_y))
        # sort points by x for sweep
        pts_sorted = sorted(points, key=lambda p: p[0])

        res_cnt = [0]*len(cands)
        pi = 0
        for x_evt, y1, y2, sign, ridx in events:
            # add all points with x < x_evt
            while pi < n and pts_sorted[pi][0] < x_evt:
                yy = pts_sorted[pi][1]
                yi = bisect.bisect_left(all_y, yy)
                fenw.add(yi, 1)
                pi += 1
            # count points with y in (y1, y2)
            # strictly inside: y1< y < y2
            i1 = bisect.bisect_right(all_y, y1)
            i2 = bisect.bisect_left(all_y, y2) - 1
            if i1 <= i2:
                cnt = fenw.range_sum(i1, i2)
            else:
                cnt = 0
            res_cnt[ridx] += sign * cnt

        # 5) pick best area among those with res_cnt==0
        ans = -1
        for (x1,x2,y1,y2,area), cnt in zip(cands, res_cnt):
            if cnt == 0 and area>ans:
                ans = area

        return ans
