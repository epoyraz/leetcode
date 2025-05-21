class Solution(object):
    def rectangleArea(self, rectangles):
        MOD = 10**9 + 7
        OPEN, CLOSE = 1, -1

        events = []
        Xvals = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            Xvals.add(x1)
            Xvals.add(x2)

        events.sort()
        Xvals = sorted(Xvals)
        Xi = {x: i for i, x in enumerate(Xvals)}

        class SegmentTreeNode:
            def __init__(self, l, r):
                self.l = l
                self.r = r
                self.left = None
                self.right = None
                self.count = 0
                self.total = 0

        def build(l, r):
            node = SegmentTreeNode(l, r)
            if l + 1 < r:
                m = (l + r) // 2
                node.left = build(l, m)
                node.right = build(m, r)
            return node

        def update(node, i, j, val):
            if node.l >= j or node.r <= i:
                return
            if i <= node.l and node.r <= j:
                node.count += val
            else:
                update(node.left, i, j, val)
                update(node.right, i, j, val)

            if node.count > 0:
                node.total = Xvals[node.r] - Xvals[node.l]
            else:
                node.total = (node.left.total if node.left else 0) + (node.right.total if node.right else 0)

        root = build(0, len(Xvals) - 1)

        prev_y = 0
        cur_x_sum = 0
        area = 0
        for y, typ, x1, x2 in events:
            area += cur_x_sum * (y - prev_y)
            area %= MOD
            update(root, Xi[x1], Xi[x2], typ)
            cur_x_sum = root.total
            prev_y = y

        return area
