class Solution:
    def minSwaps(self, s):
        c0 = s.count('0')
        c1 = len(s) - c0
        if abs(c0 - c1) > 1:
            return -1

        def count_mismatch(start):
            mismatches = 0
            for i, ch in enumerate(s):
                expected = str((i + start) % 2)
                if ch != expected:
                    mismatches += 1
            return mismatches // 2

        if c0 == c1:
            return min(count_mismatch(0), count_mismatch(1))
        elif c0 > c1:
            return count_mismatch(0)
        else:
            return count_mismatch(1)
