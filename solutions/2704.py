class Solution(object):
    def minMaxDifference(self, num):
        s = str(num)
        max_val = num
        min_val = num
        for d1 in '0123456789':
            for d2 in '0123456789':
                if d1 == d2:
                    continue
                t = s.replace(d1, d2)
                v = int(t)
                if v > max_val:
                    max_val = v
                if v < min_val:
                    min_val = v
        return max_val - min_val
