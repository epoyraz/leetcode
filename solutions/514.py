from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring, key):
        n = len(ring)
        char_pos = defaultdict(list)
        for i, ch in enumerate(ring):
            char_pos[ch].append(i)

        memo = {}

        def dp(i, pos):
            if i == len(key):
                return 0
            if (i, pos) in memo:
                return memo[(i, pos)]
            res = float('inf')
            for j in char_pos[key[i]]:
                steps = min(abs(j - pos), n - abs(j - pos)) + 1
                res = min(res, steps + dp(i + 1, j))
            memo[(i, pos)] = res
            return res

        return dp(0, 0)
