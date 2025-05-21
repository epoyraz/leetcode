import sys
sys.setrecursionlimit(10000)

class Solution:
    def maxAncestorDiff(self, root):
        self.ans = 0
        def dfs(node, lo, hi):
            if not node:
                return
            self.ans = max(self.ans, abs(node.val - lo), abs(node.val - hi))
            lo2, hi2 = min(lo, node.val), max(hi, node.val)
            dfs(node.left, lo2, hi2)
            dfs(node.right, lo2, hi2)
        dfs(root, root.val, root.val)
        return self.ans
