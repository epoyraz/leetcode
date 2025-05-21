class Solution(object):
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:
            return None
        val = (root1.val if root1 else 0) + (root2.val if root2 else 0)
        node = TreeNode(val)
        node.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        node.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        return node
