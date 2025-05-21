class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """
        # Andrew's monotone chain, keeping collinear boundary points
        pts = sorted(trees)
        if len(pts) <= 1:
            return pts

        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

        # build lower hull
        lower = []
        for p in pts:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # build upper hull
        upper = []
        for p in reversed(pts):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # concatenate, excluding duplicate endpoints
        hull = lower[:-1] + upper[:-1]
        # remove duplicates and return
        return [list(x) for x in set(map(tuple, hull))]
