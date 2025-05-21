class Solution(object):
    def minimumOperations(self, num):
        n = len(num)
        best = n
        for x, y in [('0','0'), ('2','5'), ('5','0'), ('7','5')]:
            j = num.rfind(y)
            if j == -1:
                continue
            i = num.rfind(x, 0, j)
            if i == -1:
                continue
            ops = (n - 1 - j) + (j - 1 - i)
            best = min(best, ops)
        if best == n:
            # no valid ending found: delete down to a single '0' or all digits
            if '0' in num:
                best = n - 1
            else:
                best = n
        return best
