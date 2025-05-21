class Solution:
    def closestPrimes(self, left, right):
        # Sieve of Eratosthenes up to 'right'
        n = right
        is_prime = [True] * (n + 1)
        is_prime[0:2] = [False, False]
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
            p += 1

        last = -1
        best_diff = float('inf')
        ans = [-1, -1]

        # Iterate through the range, track the closest pair
        for num in range(max(left, 2), right + 1):
            if is_prime[num]:
                if last != -1:
                    diff = num - last
                    if diff < best_diff:
                        best_diff = diff
                        ans = [last, num]
                        # Minimal possible diff is 1 for consecutive integers;
                        # primes differ by at least 2 except (2,3). We can break early
                        # if best_diff == 1 or (last == 2 and num == 3).
                        if best_diff <= 2:
                            break
                last = num

        return ans
