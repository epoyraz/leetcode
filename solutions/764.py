"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        res = []
        queue = [root]
        
        while queue:
            level = []
            next_queue = []
            for node in queue:
                level.append(node.val)
                next_queue.extend(node.children)
            res.append(level)
            queue = next_queue
        
        return res