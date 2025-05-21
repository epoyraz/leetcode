class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for a in nums1:
            for b in nums2:
                if a % (b * k) == 0:
                    count += 1
        return count
