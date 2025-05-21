class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            # push children onto stack to process before parent
            for child in node.children:
                stack.append(child)
        # reversed order gives postorder
        return res[::-1]
