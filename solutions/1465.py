class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7

        # 1) Compute total sum of all nodes
        def compute_total(node):
            if not node:
                return 0
            return node.val + compute_total(node.left) + compute_total(node.right)

        total = compute_total(root)
        self.max_prod = 0

        # 2) Compute subtree sums and update max product
        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            prod = s * (total - s)
            if prod > self.max_prod:
                self.max_prod = prod
            return s

        dfs(root)
        return self.max_prod % MOD
