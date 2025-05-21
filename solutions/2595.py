class Solution:
    def smallestValue(self, n):
        def prime_sum(x):
            s = 0
            i = 2
            while i * i <= x:
                while x % i == 0:
                    s += i
                    x //= i
                i += 1
            if x > 1:
                s += x
            return s

        prev = -1
        while n != prev:
            prev = n
            n = prime_sum(n)
        return n
