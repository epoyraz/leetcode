class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1 = sum(x for x in nums1 if x != 0)
        n1 = nums1.count(0)
        s2 = sum(x for x in nums2 if x != 0)
        n2 = nums2.count(0)

        # The smallest target sum S must satisfy:
        #   S >= s1 + n1  (so nums1's zeros can sum to S - s1 >= n1*1)
        #   S >= s2 + n2
        S = max(s1 + n1, s2 + n2)

        # Check feasibility: if an array has no zeros, its sum must already equal S.
        if (n1 > 0 or s1 == S) and (n2 > 0 or s2 == S):
            return S
        return -1
