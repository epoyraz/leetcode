# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.setrecursionlimit(10000)

class Solution:
    def removeLeafNodes(self, root, target):
        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            # If it's now a leaf with value == target, remove it
            if not node.left and not node.right and node.val == target:
                return None
            return node
        
        return dfs(root)
