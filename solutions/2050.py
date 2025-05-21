class Solution:
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7

        def mod_pow(x, y):
            res = 1
            x %= MOD
            while y:
                if y % 2:
                    res = res * x % MOD
                x = x * x % MOD
                y //= 2
            return res

        even = (n + 1) // 2
        odd = n // 2
        return mod_pow(5, even) * mod_pow(4, odd) % MOD
