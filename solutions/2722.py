class Solution:
    def diagonalPrime(self, nums):
        def is_prime(x):
            if x < 2:
                return False
            if x == 2 or x == 3:
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True

        n = len(nums)
        max_prime = 0

        for i in range(n):
            for val in [nums[i][i], nums[i][n - 1 - i]]:
                if is_prime(val):
                    max_prime = max(max_prime, val)

        return max_prime
