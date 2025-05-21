# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = second = prev = None
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev and prev.val > curr.val:
                if not first:
                    first = prev
                second = curr
            prev = curr
            curr = curr.right
        
        first.val, second.val = second.val, first.val
