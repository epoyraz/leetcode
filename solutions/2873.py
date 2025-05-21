class Solution:
    def findPrimePairs(self, n):
        if n < 3:
            return []

        # Sieve of Eratosthenes to find all primes up to n
        is_prime = [False, False] + [True] * (n - 1)
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        result = []
        for x in range(2, n // 2 + 1):
            y = n - x
            if is_prime[x] and is_prime[y]:
                result.append([x, y])

        return result
