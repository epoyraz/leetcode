class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            # compute sum of digits
            s = 0
            x = num
            while x > 0:
                s += x % 10
                x //= 10
            if s == i:
                return i
        return -1
