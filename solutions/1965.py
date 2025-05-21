class Solution(object):
    def sumBase(self, n, k):
        s = 0
        while n:
            s += n % k
            n //= k
        return s
