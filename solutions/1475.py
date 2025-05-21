class Solution(object):
    def maxSumBST(self, root):
        self.max_sum = 0

        def dfs(node):
            if not node:
                return (True, float('inf'), float('-inf'), 0)  # isBST, min, max, sum

            left_is_bst, left_min, left_max, left_sum = dfs(node.left)
            right_is_bst, right_min, right_max, right_sum = dfs(node.right)

            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                curr_sum = node.val + left_sum + right_sum
                self.max_sum = max(self.max_sum, curr_sum)
                return (True,
                        min(left_min, node.val),
                        max(right_max, node.val),
                        curr_sum)
            else:
                return (False, 0, 0, 0)

        dfs(root)
        return self.max_sum
