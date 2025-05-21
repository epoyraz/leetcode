class Solution(object):
    def findSecondMinimumValue(self, root):
        if not root or (not root.left and not root.right):
            return -1
        
        left = root.left.val
        right = root.right.val
        
        if left == root.val:
            left = self.findSecondMinimumValue(root.left)
        if right == root.val:
            right = self.findSecondMinimumValue(root.right)
        
        if left != -1 and right != -1:
            return min(left, right)
        if left != -1:
            return left
        return right
