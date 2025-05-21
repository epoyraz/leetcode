class Solution(object):
    def minimumTime(self, s):
        n = len(s)
        res = n  # worst case: remove every character one-by-one from the ends (all 1s)
        left = 0

        for i in range(n):
            if s[i] == '1':
                left = min(left + 2, i + 1)  # remove s[i] (2 units) vs remove from left (1 unit each)
            res = min(res, left + n - 1 - i)  # left side cost + right side cost
        return res
