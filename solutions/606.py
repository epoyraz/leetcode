# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        
        s = str(t.val)
        
        # If there is a right child but no left child, we need "()"
        if not t.left and t.right:
            s += "()"
        
        # Recurse on left child if exists
        if t.left:
            s += "(" + self.tree2str(t.left) + ")"
        
        # Recurse on right child if exists
        if t.right:
            s += "(" + self.tree2str(t.right) + ")"
        
        return s
