class Solution(object):
    def addOneRow(self, root, val, depth):
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        def dfs(node, current_depth):
            if not node:
                return
            if current_depth == depth - 1:
                left = TreeNode(val)
                right = TreeNode(val)
                left.left = node.left
                right.right = node.right
                node.left = left
                node.right = right
            else:
                dfs(node.left, current_depth + 1)
                dfs(node.right, current_depth + 1)
        
        dfs(root, 1)
        return root
