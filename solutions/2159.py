class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict

        count = defaultdict(int)

        for num in set(nums1):
            count[num] += 1
        for num in set(nums2):
            count[num] += 1
        for num in set(nums3):
            count[num] += 1

        result = []
        for num in count:
            if count[num] >= 2:
                result.append(num)

        return result
