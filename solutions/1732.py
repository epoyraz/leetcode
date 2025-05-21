class Solution:
    def minimumOneBitOperations(self, n):
        memo = {}

        def f(x):
            # base cases
            if x < 2:
                return x
            if x in memo:
                return memo[x]

            m = x.bit_length() - 1
            high = 1 << m
            # use the recurrence: f(x) = (2^(m+1)-1) - f(x - 2^m)
            res = (high << 1) - 1 - f(x - high)

            memo[x] = res
            return res

        return f(n)
