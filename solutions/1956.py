class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        cur = 1
        for x in arr:
            if x >= cur:
                cur += 1
        return cur - 1
