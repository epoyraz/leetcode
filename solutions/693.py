class Solution(object):
    def hasAlternatingBits(self, n):
        last = n & 1
        n >>= 1
        while n:
            curr = n & 1
            if curr == last:
                return False
            last = curr
            n >>= 1
        return True
