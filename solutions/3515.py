class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_single = 0
        sum_double = 0
        for x in nums:
            if x < 10:
                sum_single += x
            else:
                sum_double += x
        # Alice can choose single-digit or double-digit numbers
        return sum_single > sum_double or sum_double > sum_single
