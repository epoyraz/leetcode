class Solution(object):
    def pivotInteger(self, n):
        total = n * (n + 1) // 2
        r = int(total**0.5)
        return r if r * r == total else -1
