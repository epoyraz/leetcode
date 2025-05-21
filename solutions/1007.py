class Solution:
    def numsSameConsecDiff(self, n, k):
        res = []

        def dfs(num, length):
            if length == n:
                res.append(num)
                return
            last_digit = num % 10
            next_digits = set()
            if last_digit + k < 10:
                next_digits.add(last_digit + k)
            if last_digit - k >= 0:
                next_digits.add(last_digit - k)
            for d in next_digits:
                dfs(num * 10 + d, length + 1)

        for i in range(1, 10):  # no leading zero
            dfs(i, 1)

        return res
