class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Compute diff[i] = distinct count prefix nums[0..i] - distinct count suffix nums[i+1..n-1]
        """
        n = len(nums)
        result = [0] * n
        for i in range(n):
            prefix = set(nums[:i+1])
            suffix = set(nums[i+1:])
            result[i] = len(prefix) - len(suffix)
        return result