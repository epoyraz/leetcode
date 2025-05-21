class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ops = 0
        
        # Walk from i=0 up to i=n-3.
        # Whenever nums[i] is 0, we flip [i, i+1, i+2].
        for i in range(n-2):
            if nums[i] == 0:
                # perform the flip
                nums[i]   ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                ops += 1
        
        # After that, positions n-2 and n-1 cannot be changed again.
        # If either is 0, it's impossible.
        if nums[-2] == 0 or nums[-1] == 0:
            return -1
        return ops
