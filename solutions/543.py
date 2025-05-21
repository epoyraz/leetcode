class Solution:
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return max(left, right) + 1

        depth(root)
        return self.max_diameter
