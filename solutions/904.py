class Solution(object):
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + dfs(node.right)
        
        return dfs(root1) == dfs(root2)
