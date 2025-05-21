class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        n = len(nums)
        keep = set()
        for i, v in enumerate(nums):
            if v == key:
                keep.update(xrange(max(0, i - k), min(n - 1, i + k) + 1))
        return sorted(keep)
