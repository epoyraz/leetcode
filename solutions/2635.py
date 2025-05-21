class Solution:
    def isReachable(self, targetX, targetY):
        # Compute gcd with Euclid's algorithm
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = gcd(targetX, targetY)
        # Check if g is a power of two (including 1)
        return g > 0 and (g & (g - 1)) == 0
