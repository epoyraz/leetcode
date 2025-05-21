class Solution(object):
    def passThePillow(self, n, time):
        cycle = 2 * (n - 1)
        t = time % cycle
        if t < n:
            return 1 + t
        else:
            return 2 * n - 1 - t
