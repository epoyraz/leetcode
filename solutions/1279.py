class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        # Count how many primes <= n
        prime_count = sum(is_prime(i) for i in range(1, n + 1))

        # Compute factorial with modulo
        def factorial(x):
            res = 1
            for i in range(2, x + 1):
                res = (res * i) % MOD
            return res

        return (factorial(prime_count) * factorial(n - prime_count)) % MOD
