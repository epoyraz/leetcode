class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_xor = 0
        
        for i in range(n):
            x = nums[i]
            for j in range(n):
                y = nums[j]
                # check strong pair: |x - y| <= min(x, y)
                if abs(x - y) <= min(x, y):
                    max_xor = max(max_xor, x ^ y)
        
        return max_xor