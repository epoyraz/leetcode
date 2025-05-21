class Solution(object):
    def primePalindrome(self, n):
        def is_prime(x):
            if x < 2: return False
            if x == 2: return True
            if x % 2 == 0: return False
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True
        
        if 8 <= n <= 11:
            return 11

        for length in range(1, 6):
            for half in range(10**(length - 1), 10**length):
                s = str(half)
                p = int(s + s[-2::-1])
                if p >= n and is_prime(p):
                    return p
