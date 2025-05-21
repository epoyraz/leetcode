class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        L = postorder.index(preorder[1]) + 1
        root.left = self.constructFromPrePost(preorder[1:L+1], postorder[:L])
        root.right = self.constructFromPrePost(preorder[L+1:], postorder[L:-1])
        return root