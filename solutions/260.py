class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num

        diff = xor & -xor
        
        a = 0
        for num in nums:
            if num & diff:
                a ^= num

        return [a, xor ^ a]
