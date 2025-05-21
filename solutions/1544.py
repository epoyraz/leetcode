class Solution(object):
    def goodNodes(self, root):
        def dfs(node, max_so_far):
            if not node:
                return 0
            count = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            return count

        return dfs(root, root.val)
