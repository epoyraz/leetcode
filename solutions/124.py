# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursively get max path sum from left and right
            left_gain = max(dfs(node.left), 0)  # we ignore negative paths
            right_gain = max(dfs(node.right), 0)
            
            # Price of the new path starting from this node
            price_newpath = node.val + left_gain + right_gain
            
            # Update the global max_sum
            self.max_sum = max(self.max_sum, price_newpath)
            
            # For recursion: return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self.max_sum
