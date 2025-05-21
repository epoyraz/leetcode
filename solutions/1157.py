class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        def dfs(node, sum_so_far):
            if not node:
                return None
            sum_so_far += node.val
            if not node.left and not node.right:
                return node if sum_so_far >= limit else None
            node.left = dfs(node.left, sum_so_far)
            node.right = dfs(node.right, sum_so_far)
            return node if node.left or node.right else None
        
        return dfs(root, 0)
