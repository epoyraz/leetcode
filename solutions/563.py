class Solution(object):
    def findTilt(self, root):
        self.tilt = 0

        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            self.tilt += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val

        dfs(root)
        return self.tilt
