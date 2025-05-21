class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        stack = [root]
        for v in preorder[1:]:
            node = TreeNode(v)
            if v < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and stack[-1].val < v:
                    last = stack.pop()
                last.right = node
                stack.append(node)
        return root
