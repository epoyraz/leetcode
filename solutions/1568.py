# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pseudoPalindromicPaths(self, root):
        self.count = 0
        
        def dfs(node, mask):
            if not node:
                return
            # toggle the bit corresponding to node.val
            mask ^= 1 << node.val
            # if it's a leaf, check if at most one bit is set in mask
            if not node.left and not node.right:
                # mask & (mask - 1) == 0 means at most one bit set
                if mask & (mask - 1) == 0:
                    self.count += 1
            else:
                dfs(node.left, mask)
                dfs(node.right, mask)
        
        dfs(root, 0)
        return self.count
