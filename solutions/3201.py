class Solution:
    def distributeCandies(self, n, limit):
        def comb(n, k):
            if k < 0 or k > n:
                return 0
            res = 1
            for i in range(1, k + 1):
                res = res * (n - i + 1) // i
            return res

        def count(x):
            return comb(x + 2, 2) if x >= 0 else 0

        l = limit + 1
        total = count(n)
        over1 = count(n - l)
        over2 = count(n - 2 * l)
        over3 = count(n - 3 * l)

        return total - 3 * over1 + 3 * over2 - over3
