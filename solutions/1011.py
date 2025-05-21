class Solution:
    def flipMatchVoyage(self, root, voyage):
        self.i = 0
        self.res = []

        def dfs(node):
            if not node:
                return True
            if node.val != voyage[self.i]:
                return False
            self.i += 1
            if node.left and node.left.val != voyage[self.i]:
                # Flip needed
                self.res.append(node.val)
                return dfs(node.right) and dfs(node.left)
            return dfs(node.left) and dfs(node.right)

        return self.res if dfs(root) else [-1]
