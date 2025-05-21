class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0]*n
        for i, v in enumerate(nums):
            # (i + v) % n handles both positive and negative steps
            j = (i + v) % n
            result[i] = nums[j]
        return result
