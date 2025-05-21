class Solution:
    def minimumSwap(self, s1, s2):
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1

        if (xy + yx) % 2 != 0:
            return -1

        return xy // 2 + yx // 2 + (xy % 2) * 2
