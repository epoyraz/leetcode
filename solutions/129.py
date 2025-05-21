# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, current_num):
            if not node:
                return 0
            
            # Update the current number
            current_num = current_num * 10 + node.val
            
            # If this is a leaf node, return the current path's number
            if not node.left and not node.right:
                return current_num
            
            # Otherwise, recurse on left and right children
            left_sum = dfs(node.left, current_num)
            right_sum = dfs(node.right, current_num)
            
            return left_sum + right_sum
        
        return dfs(root, 0)