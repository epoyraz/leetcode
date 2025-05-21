class Solution(object):
    def replaceNonCoprimes(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        stack = []
        for x in nums:
            stack.append(x)
            while len(stack) > 1:
                g = gcd(stack[-1], stack[-2])
                if g == 1:
                    break
                lcm = stack[-2] // g * stack[-1]
                stack.pop()
                stack[-1] = lcm
        return stack
