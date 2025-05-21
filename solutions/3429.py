class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Iterate over each adjacent pair
        for i in range(1, len(nums)):
            # If both even or both odd, parity is the same â not special
            if nums[i] % 2 == nums[i-1] % 2:
                return False
        # If we never found a same-parity pair, it's special
        return True
