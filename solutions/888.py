class Solution(object):
    def mirrorReflection(self, p, q):
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2
        if p % 2 == 0 and q % 2 == 1:
            return 2
        if p % 2 == 1 and q % 2 == 0:
            return 0
        return 1
