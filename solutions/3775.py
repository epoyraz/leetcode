class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        # 1) Build events for the vertical sweep
        events = []   # (y, type, x1, x2)
        xs = []
        for x, y, l in squares:
            events.append((y,     1, x,     x + l))
            events.append((y + l, -1, x,     x + l))
            xs.extend((x, x + l))
        if not events:
            return 0.0

        # 2) Coordinate-compress the x-endpoints
        coords = sorted(set(xs))
        idx = {v:i for i, v in enumerate(coords)}
        M = len(coords)

        # 3) Segment-tree to maintain total covered x-length under current active squares
        class SegTree:
            def __init__(self, coords):
                self.coords = coords
                self.n = len(coords)
                self.count = [0] * (4 * self.n)
                self.covered = [0] * (4 * self.n)

            def update(self, node, l, r, ql, qr, val):
                # no overlap
                if ql >= r or qr <= l:
                    return
                # full cover
                if ql <= l and r <= qr:
                    self.count[node] += val
                else:
                    mid = (l + r) // 2
                    self.update(node*2,     l,   mid, ql, qr, val)
                    self.update(node*2 + 1, mid,   r,  ql, qr, val)

                # recalc covered length
                if self.count[node] > 0:
                    # fully covered
                    self.covered[node] = self.coords[r] - self.coords[l]
                else:
                    if l + 1 == r:
                        # leaf segment
                        self.covered[node] = 0
                    else:
                        self.covered[node] = (
                            self.covered[node*2] +
                            self.covered[node*2 + 1]
                        )

            def total_covered(self):
                return self.covered[1]

        # 4) Sort events by y, sweep to build slabs of constant width
        events.sort(key=lambda e: e[0])
        st = SegTree(coords)

        slabs = []   # list of (y_start, y_end, width)
        prev_y = events[0][0]
        i = 0
        n_ev = len(events)

        while i < n_ev:
            y = events[i][0]
            dy = y - prev_y
            if dy > 0:
                width = st.total_covered()
                if width > 0:
                    slabs.append((prev_y, y, width))
                prev_y = y

            # process all events at this y
            while i < n_ev and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                l = idx[x1]
                r = idx[x2]
                st.update(1, 0, M-1, l, r, typ)
                i += 1

        # 5) Compute total union area and then find the half-area cut
        total = 0.0
        for y0, y1, w in slabs:
            total += w * (y1 - y0)
        half = total / 2.0

        acc = 0.0
        for y0, y1, w in slabs:
            segment_area = w * (y1 - y0)
            if acc + segment_area >= half:
                # the cut lies in this slab
                remain = half - acc
                return y0 + remain / w
            acc += segment_area

        # If we haven't returned yet, the cut is at or above the last event
        return float(slabs[-1][1])
