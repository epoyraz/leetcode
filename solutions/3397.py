class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # Sort both arrays
        nums1_sorted = sorted(nums1)
        nums2_sorted = sorted(nums2)
        # The difference between any corresponding elements is the same x
        return nums2_sorted[0] - nums1_sorted[0]
