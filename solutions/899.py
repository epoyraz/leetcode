class Solution(object):
    def binaryGap(self, n):
        last = -1
        max_gap = 0
        i = 0
        while n:
            if n & 1:
                if last != -1:
                    max_gap = max(max_gap, i - last)
                last = i
            n >>= 1
            i += 1
        return max_gap
