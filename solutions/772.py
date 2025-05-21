"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid):
        def build(x0, y0, size):
            if size == 1:
                return Node(bool(grid[x0][y0]), True)
            
            half = size // 2
            tl = build(x0, y0, half)
            tr = build(x0, y0 + half, half)
            bl = build(x0 + half, y0, half)
            br = build(x0 + half, y0 + half, half)
            
            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
                return Node(tl.val, True)
            else:
                return Node(True, False, tl, tr, bl, br)
        
        n = len(grid)
        return build(0, 0, n)