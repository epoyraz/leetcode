# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthLargestPerfectSubtree(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        perfect_sizes = []

        def dfs(node):
            if not node:
                return True, 0, 0  # is_perfect, depth, size
            
            left_perfect, left_depth, left_size = dfs(node.left)
            right_perfect, right_depth, right_size = dfs(node.right)
            
            if left_perfect and right_perfect and left_depth == right_depth:
                size = left_size + right_size + 1
                depth = left_depth + 1
                perfect_sizes.append(size)
                return True, depth, size
            else:
                return False, 0, 0

        dfs(root)

        perfect_sizes.sort(reverse=True)
        return perfect_sizes[k - 1] if k <= len(perfect_sizes) else -1
