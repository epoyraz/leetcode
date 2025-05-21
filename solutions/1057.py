import math

class Solution:
    def numDupDigitsAtMostN(self, n):
        def perm(a, b):
            res = 1
            for i in range(b):
                res *= a - i
            return res

        def countUniqueDigits(x):
            s = list(map(int, str(x)))
            n_digits = len(s)
            res = 0

            # Count numbers with digits less than n_digits
            for i in range(1, n_digits):
                res += 9 * perm(9, i - 1)

            # Count numbers with digits == n_digits
            used = set()
            for i in range(n_digits):
                for d in range(0 if i else 1, s[i]):
                    if d in used:
                        continue
                    res += perm(9 - i, n_digits - i - 1)
                if s[i] in used:
                    break
                used.add(s[i])
            else:
                res += 1  # count x itself if all digits are unique

            return res

        return n - countUniqueDigits(n)
