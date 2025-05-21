import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = collections.Counter(nums1)
        res = []
        for num in nums2:
            if count1[num] > 0:
                res.append(num)
                count1[num] -= 1
        return res
