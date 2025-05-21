class Solution:
    def appealSum(self, s):
        n = len(s)
        last = {c: -1 for c in "abcdefghijklmnopqrstuvwxyz"}
        total = 0
        for i, ch in enumerate(s):
            prev = last[ch]
            total += (i - prev) * (n - i)
            last[ch] = i
        return total
