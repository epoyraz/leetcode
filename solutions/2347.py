# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root):
        self.ans = 0
        
        def dfs(node):
            # returns (sum of subtree, count of nodes)
            if not node:
                return (0, 0)
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            total_sum = ls + rs + node.val
            total_count = lc + rc + 1
            # integer average (floored)
            if node.val == total_sum // total_count:
                self.ans += 1
            return (total_sum, total_count)
        
        dfs(root)
        return self.ans
