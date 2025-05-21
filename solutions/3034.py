class Solution(object):
    def numberOfPoints(self, nums):
        # Since 1 <= starti <= endi <= 100, we can mark each integer point.
        covered = [0] * 101
        for a, b in nums:
            for x in range(a, b + 1):
                covered[x] = 1
        return sum(covered)
