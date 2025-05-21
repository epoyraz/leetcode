class Solution(object):
    def evenOddBit(self, n):
        even = odd = 0
        idx = 0
        while n:
            if n & 1:
                if idx % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>= 1
            idx += 1
        return [even, odd]
