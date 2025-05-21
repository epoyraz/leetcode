import bisect

class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # longest strictlyâincreasing prefix ends at P
        P = 0
        while P + 1 < n and nums[P + 1] > nums[P]:
            P += 1
        # earliest strictlyâincreasing suffix starts at S
        S = n - 1
        while S - 1 >= 0 and nums[S] > nums[S - 1]:
            S -= 1
        # we can only start removals up to l_max
        l_max = min(P + 1, n - 1)
        total = 0
        for l in range(l_max + 1):
            # minimal r so that suffix from r+1... is increasing
            r_min = max(l, S - 1)
            if l == 0:
                # no prefix to worry about
                total += n - r_min
            else:
                # need nums[l-1] < nums[r+1] for r < n-1
                threshold = nums[l - 1]
                k_start = r_min + 1
                if k_start > n - 1:
                    total += 1  # only r = n-1
                else:
                    # binary search in the strictly increasing tail [k_start..n-1]
                    k0 = bisect.bisect_right(nums, threshold, k_start, n)
                    # k in [k0..n-1] â r = k-1 in [r_min..n-2], plus r=n-1
                    total += (n - k0) + 1
        return total
