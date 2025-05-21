class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        # Number of cuts we make between segments
        cuts = 0
        
        # Maximum of the last completed segment (conceptually -inf)
        last_max = float('-inf')
        # Maximum of the current (in-progress) segment
        curr_max = nums[0]
        
        # Try to cut before each position i = 1..n-1
        for i in range(1, n):
            x = nums[i]
            if x >= curr_max:
                # We can end the previous segment here:
                #   its max = curr_max â¤ x â¤ eventual max of next segment
                cuts += 1
                last_max = curr_max
                curr_max = x
            else:
                # Must absorb x into current segment to keep its max â¥ x
                # (and thus be able to compare to the next segment later)
                curr_max = max(curr_max, x)
        
        # Segments = cuts + 1 â that's the maximum non-decreasing size
        return cuts + 1
