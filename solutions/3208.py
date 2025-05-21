from collections import defaultdict
import math

class Solution:
    def beautifulSubstrings(self, s, k):
        # 1) compute g = â p^{ceil(e/2)} for k's prime factorization
        g = 1
        temp = k
        p = 2
        while p * p <= temp:
            if temp % p == 0:
                e = 0
                while temp % p == 0:
                    temp //= p
                    e += 1
                g *= p ** ((e + 1) // 2)
            p += 1
        if temp > 1:
            # remaining prime factor
            g *= temp

        # 2) scan prefixes
        freq = defaultdict(int)
        D = 0    # vowel_count - consonant_count
        V = 0    # vowel count
        # empty prefix at position 0:
        freq[(0, 0)] = 1

        res = 0
        vowels = set('aeiou')

        for ch in s:
            if ch in vowels:
                V += 1
                D += 1
            else:
                D -= 1

            r = V % g
            # all previous prefixes with same (D, r) form valid substrings
            res += freq[(D, r)]
            freq[(D, r)] += 1

        return res
