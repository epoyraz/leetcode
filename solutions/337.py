

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return (rob, not_rob)
        
        return max(dfs(root))
