class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # The bitwise OR of a set of numbers is even (has at least one trailing zero)
        # if and only if all numbers in the set are even (their LSB is 0).
        # So we just need at least two even numbers.
        evens = sum(1 for x in nums if x % 2 == 0)
        return evens >= 2
