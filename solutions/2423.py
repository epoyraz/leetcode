class Solution:
    def minOperations(self, nums, numsDivide):
        # local gcd implementation to avoid relying on math.gcd
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Compute gcd of all elements in numsDivide
        g = numsDivide[0]
        for x in numsDivide[1:]:
            g = gcd(g, x)
        
        # Sort nums so that the first valid divisor yields minimal deletions
        nums.sort()
        
        # Find the smallest nums[i] that divides g
        for i, x in enumerate(nums):
            if g % x == 0:
                return i
        
        return -1
