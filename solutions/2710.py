class Solution(object):
    def minOperations(self, n):
        ops = 0
        while n > 0:
            if n & 1 == 0:
                # even: no Â±-2á¶¦ operation needed, just shift
                n >>= 1
            else:
                # odd: decide whether to +1 or â1
                # best to subtract when n%4==1 or n==3; otherwise add
                if n == 3 or (n & 3) == 1:
                    n -= 1
                else:
                    n += 1
                ops += 1
                n >>= 1
        return ops
