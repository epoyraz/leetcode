class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            found = False
            for x in range(num):
                if (x | (x + 1)) == num:
                    res.append(x)
                    found = True
                    break
            if not found:
                res.append(-1)
        return res
