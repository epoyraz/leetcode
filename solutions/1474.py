class Solution(object):
    def longestZigZag(self, root):
        self.max_len = 0

        def dfs(node, direction, length):
            if not node:
                return
            self.max_len = max(self.max_len, length)
            if direction == 'left':
                dfs(node.left, 'right', length + 1)
                dfs(node.right, 'left', 1)
            else:
                dfs(node.right, 'left', length + 1)
                dfs(node.left, 'right', 1)

        dfs(root.left, 'right', 1)
        dfs(root.right, 'left', 1)

        return self.max_len
