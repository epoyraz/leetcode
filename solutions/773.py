# Definition for a QuadTree node.
# class Node(object):
#     def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight

class Solution(object):
    def intersect(self, q1, q2):
        # if either is a leaf:
        if q1.isLeaf:
            # if q1 is leaf 1, OR is all 1s
            if q1.val:
                return Node(True, True)
            # else result is q2
            return q2
        if q2.isLeaf:
            if q2.val:
                return Node(True, True)
            return q1

        # both internal: recurse on children
        tl = self.intersect(q1.topLeft, q2.topLeft)
        tr = self.intersect(q1.topRight, q2.topRight)
        bl = self.intersect(q1.bottomLeft, q2.bottomLeft)
        br = self.intersect(q1.bottomRight, q2.bottomRight)

        # if all four children are leaves and have same value, merge
        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and \
           tl.val == tr.val == bl.val == br.val:
            return Node(tl.val, True)

        # otherwise return internal node (val can be anything)
        return Node(False, False, tl, tr, bl, br)
