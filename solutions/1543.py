class Solution(object):
    def simplifiedFractions(self, n):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        res = []
        for d in range(2, n + 1):
            for num in range(1, d):
                if gcd(num, d) == 1:
                    res.append(str(num) + "/" + str(d))
        return res
