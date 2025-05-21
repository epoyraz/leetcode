class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        self.count = 0

        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [1]  # Leaf node: distance 1 from itself

            left = dfs(node.left)
            right = dfs(node.right)

            # Count good leaf pairs between left and right
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.count += 1

            # Return updated distances to parent (incremented by 1)
            return [x + 1 for x in left + right if x + 1 <= distance]

        dfs(root)
        return self.count
