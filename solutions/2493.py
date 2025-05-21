from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        q = deque([root])
        level = 0
        
        while q:
            size = len(q)
            nodes = []
            for _ in range(size):
                node = q.popleft()
                nodes.append(node)
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
            
            # Reverse values at odd levels
            if level % 2 == 1:
                vals = [node.val for node in nodes]
                for node, v in zip(nodes, reversed(vals)):
                    node.val = v
            
            level += 1
        
        return root
