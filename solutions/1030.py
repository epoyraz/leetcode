class Solution:
    def smallestFromLeaf(self, root):
        self.smallest = "~"  # '~' is lex greater than any lowercase string

        def dfs(node, path):
            if not node:
                return
            # Prepend current character to path
            path = chr(ord('a') + node.val) + path
            if not node.left and not node.right:
                self.smallest = min(self.smallest, path)
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return self.smallest
