class Solution:
    def chalkReplacer(self, chalk, k):
        total = sum(chalk)
        k %= total
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c
