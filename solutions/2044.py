from collections import defaultdict

class Solution:
    def wonderfulSubstrings(self, word):
        count = defaultdict(int)
        count[0] = 1  # base case: empty prefix
        res = 0
        mask = 0

        for ch in word:
            bit = ord(ch) - ord('a')
            mask ^= (1 << bit)

            res += count[mask]  # same mask -> all even

            for i in range(10):  # one odd letter
                res += count[mask ^ (1 << i)]

            count[mask] += 1

        return res
