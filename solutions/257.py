# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        
        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            dfs(node.left, path + str(node.val) + "->")
            dfs(node.right, path + str(node.val) + "->")
        
        dfs(root, "")
        return res
