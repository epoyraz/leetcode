class Solution:
    def maximumsSplicedArray(self, nums1, nums2):
        def kadane(diff):
            max_ending_here = max_so_far = diff[0]
            for x in diff[1:]:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max(0, max_so_far)  # No swap is also valid

        s1 = sum(nums1)
        s2 = sum(nums2)

        diff1 = [b - a for a, b in zip(nums1, nums2)]
        diff2 = [a - b for a, b in zip(nums1, nums2)]

        return max(s1 + kadane(diff1), s2 + kadane(diff2))
