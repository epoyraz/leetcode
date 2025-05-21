class Solution:
    def insertIntoMaxTree(self, root, val):
        if not root:
            return TreeNode(val)
        if val > root.val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
