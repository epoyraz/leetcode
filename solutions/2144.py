class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        max_diff = -1
        for num in nums[1:]:
            if num > min_val:
                max_diff = max(max_diff, num - min_val)
            else:
                min_val = num
        return max_diff
