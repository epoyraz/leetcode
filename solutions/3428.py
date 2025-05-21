class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        dup = set()
        for x in nums:
            if x in seen:
                dup.add(x)
            else:
                seen.add(x)

        res = 0
        for x in dup:
            res ^= x
        return res
