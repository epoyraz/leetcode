class Solution:
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        result = []
        for i, v in enumerate(nums):
            if v == target:
                result.append(i)
        return result
