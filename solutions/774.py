"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        max_child_depth = 0
        for child in root.children:
            max_child_depth = max(max_child_depth, self.maxDepth(child))
        return max_child_depth + 1

        