class Solution:
    def isGoodArray(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = nums[0]
        for num in nums[1:]:
            g = gcd(g, num)
        return g == 1
