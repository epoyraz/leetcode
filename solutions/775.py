class Solution(object):
    def preorder(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # push children in reverse order so we process left-to-right
            for child in reversed(node.children):
                stack.append(child)
        return res
