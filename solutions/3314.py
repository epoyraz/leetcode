class Solution(object):
    def mostFrequentPrime(self, mat):
        from collections import defaultdict

        # Check if number is prime (only called for numbers > 10)
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True

        m, n = len(mat), len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        count = defaultdict(int)

        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    x, y = i, j
                    num = ''
                    while 0 <= x < m and 0 <= y < n:
                        num += str(mat[x][y])
                        val = int(num)
                        if val > 10 and is_prime(val):
                            count[val] += 1
                        x += dx
                        y += dy

        if not count:
            return -1

        max_freq = max(count.values())
        best = -1
        for num in count:
            if count[num] == max_freq:
                best = max(best, num)
        return best
