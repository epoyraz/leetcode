import bisect

class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        # ensure nums1 is the shorter
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # compute true bounds from all 4 corners
        candidates = [
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1],
        ]
        lo, hi = min(candidates), max(candidates)

        def count_no_greater(x):
            # count pairs (a,b) with a*b <= x
            total = 0
            n2 = len(nums2)
            for a in nums1:
                if a == 0:
                    if x >= 0:
                        total += n2
                elif a > 0:
                    bound = x // a
                    total += bisect.bisect_right(nums2, bound)
                else:  # a < 0
                    # ceil(x / a) = -floor(-x / a)
                    need = -((-x) // a)
                    idx = bisect.bisect_left(nums2, need)
                    total += n2 - idx
            return total

        # binary search for smallest mid with count >= k
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if count_no_greater(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
