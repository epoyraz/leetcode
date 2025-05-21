import re

class Solution(object):
    def fractionAddition(self, expression):
        # helper gcd for Python versions without math.gcd
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Extract all signed fractions
        tokens = re.findall(r'[+-]?\d+/\d+', expression)

        # Start with 0/1
        num, den = 0, 1

        for token in tokens:
            a_str, b_str = token.split('/')
            a, b = int(a_str), int(b_str)
            # Add a/b to num/den:
            #   num/den + a/b = (num*b + a*den) / (den*b)
            num = num * b + a * den
            den = den * b
            # Reduce
            g = gcd(abs(num), den)
            num //= g
            den //= g

        # If result is zero, force denominator = 1
        if num == 0:
            den = 1

        return str(num) + '/' + str(den)
