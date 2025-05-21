class Solution:
    def minFlips(self, a, b, c):
        flips = 0
        while a or b or c:
            ai = a & 1
            bi = b & 1
            ci = c & 1

            if ci:
                # Need at least one of ai or bi to be 1
                if ai == 0 and bi == 0:
                    flips += 1
            else:
                # Both ai and bi must be 0
                flips += ai + bi

            a >>= 1
            b >>= 1
            c >>= 1

        return flips
