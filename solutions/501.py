class Solution:
    def findMode(self, root):
        self.prev = None
        self.count = 0
        self.max_count = 0
        self.modes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is None or self.prev != node.val:
                self.count = 1
            else:
                self.count += 1
            if self.count > self.max_count:
                self.max_count = self.count
                self.modes = [node.val]
            elif self.count == self.max_count:
                self.modes.append(node.val)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.modes
