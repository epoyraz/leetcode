class Solution:
    def kMirror(self, k, n):
        def is_pal_base_k(x):
            # Check if x in base-k is a palindrome
            digits = []
            while x > 0:
                digits.append(x % k)
                x //= k
            return digits == digits[::-1]

        def gen_palindromes():
            # Yield base-10 palindromes in ascending order
            # 1-digit:
            for d in range(1, 10):
                yield d
            length = 2
            while True:
                half = (length + 1) // 2
                start = 10**(half - 1)
                end = 10**half
                for first in range(start, end):
                    s = str(first)
                    if length % 2 == 1:
                        pal = s + s[-2::-1]
                    else:
                        pal = s + s[::-1]
                    yield int(pal)
                length += 1

        result = []
        for p in gen_palindromes():
            if is_pal_base_k(p):
                result.append(p)
                if len(result) == n:
                    break
        return sum(result)
