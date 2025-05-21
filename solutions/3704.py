class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        # If overall sum is odd, diff = 2*prefix - total is odd for all prefixes
        if total % 2 != 0:
            return 0
        # Otherwise every split between 0..n-2 is valid
        return len(nums) - 1
