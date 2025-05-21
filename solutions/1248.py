class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.left_count = 0
        self.right_count = 0
        
        def count_nodes(node):
            if not node:
                return 0
            left = count_nodes(node.left)
            right = count_nodes(node.right)
            if node.val == x:
                self.left_count = left
                self.right_count = right
            return left + right + 1
        
        count_nodes(root)
        
        parent_count = n - (self.left_count + self.right_count + 1)
        max_region = max(self.left_count, self.right_count, parent_count)
        
        return max_region > n // 2
