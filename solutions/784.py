class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            from collections import deque
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
