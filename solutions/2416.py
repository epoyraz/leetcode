class Solution:
    def evaluateTree(self, root):
        # If it's a leaf, return its boolean value
        if not root.left and not root.right:
            return bool(root.val)
        
        # Evaluate children
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        
        # 2 = OR, 3 = AND
        if root.val == 2:
            return left_val or right_val
        else:
            return left_val and right_val
