class Solution:
    def beautifulArray(self, n):
        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return [1]
            odd = helper((n + 1) // 2)
            even = helper(n // 2)
            res = [2 * x - 1 for x in odd] + [2 * x for x in even]
            memo[n] = res
            return res

        return helper(n)
