class Solution:
    def numberOfCuts(self, n):
        # Special case: one slice needs no cuts
        if n == 1:
            return 0
        # For even n, each diameter cut creates two slice boundaries
        if n % 2 == 0:
            return n // 2
        # For odd n > 1, only radial cuts are possible
        return n
