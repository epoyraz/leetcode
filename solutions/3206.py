class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set2 = set(nums2)
        # Count how many in nums1 appear in nums2
        answer1 = sum(1 for x in nums1 if x in set2)
        
        set1 = set(nums1)
        # Count how many in nums2 appear in nums1
        answer2 = sum(1 for x in nums2 if x in set1)
        
        return [answer1, answer2]
