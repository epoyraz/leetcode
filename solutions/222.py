# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(node, isLeft):
            depth = 0
            while node:
                node = node.left if isLeft else node.right
                depth += 1
            return depth
        
        if not root:
            return 0
        
        left_depth = getDepth(root.left, True)
        right_depth = getDepth(root.right, False)
        
        if left_depth == right_depth:
            return (1 << (left_depth + 1)) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
