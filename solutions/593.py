class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dist2(a, b):
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            return dx*dx + dy*dy

        pts = [p1, p2, p3, p4]
        dists = []
        # compute all squared distances between pairs
        for i in range(4):
            for j in range(i+1, 4):
                dists.append(dist2(pts[i], pts[j]))
        dists.sort()
        # For a square:
        # - first 4 distances (sides) are equal and > 0
        # - last 2 distances (diagonals) are equal
        # - diagonal^2 == 2 * side^2
        side = dists[0]
        if side == 0:
            return False
        # check 4 sides equal
        for i in range(1, 4):
            if dists[i] != side:
                return False
        # check 2 diagonals equal
        if dists[4] != dists[5]:
            return False
        # check diagonal relation: diagonal == 2 * side
        if dists[4] != 2 * side:
            return False
        return True
