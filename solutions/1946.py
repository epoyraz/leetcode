import bisect

class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        MOD = 10**9 + 7
        n = len(nums1)
        sorted1 = sorted(nums1)
        total = 0
        max_gain = 0
        for a, b in zip(nums1, nums2):
            diff = abs(a - b)
            total += diff
            # find in sorted1 the closest to b
            idx = bisect.bisect_left(sorted1, b)
            best = diff
            if idx < n:
                best = min(best, abs(sorted1[idx] - b))
            if idx > 0:
                best = min(best, abs(sorted1[idx-1] - b))
            gain = diff - best
            if gain > max_gain:
                max_gain = gain
        return (total - max_gain) % MOD
