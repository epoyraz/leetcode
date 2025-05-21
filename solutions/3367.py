class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for x in nums:
            s = str(x)
            m = max(s)
            total += int(m * len(s))
        return total
