class Solution(object):
    def allPossibleFBT(self, n):
        memo = {}

        def build(t):
            if t in memo:
                return memo[t]
            if t == 1:
                return [TreeNode(0)]
            res = []
            for i in range(1, t, 2):
                for left in build(i):
                    for right in build(t - 1 - i):
                        res.append(TreeNode(0, left, right))
            memo[t] = res
            return res

        return build(n) if n % 2 == 1 else []