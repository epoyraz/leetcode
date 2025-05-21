class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sum each positive value exactly once:
        total = sum({x for x in nums if x > 0})
        if total > 0:
            return total
        # Otherwise no positives â pick the single largest element
        return max(nums)
