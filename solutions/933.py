class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            node.left = None
            self.curr.right = node
            self.curr = node
            inorder(node.right)

        dummy = TreeNode(0)
        self.curr = dummy
        inorder(root)
        return dummy.right
