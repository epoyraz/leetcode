class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Since n >= 2 by constraint, we can initialize to zero safely
        max_diff = 0
        
        # Compare each pair of consecutive elements
        for i in range(1, n):
            diff = abs(nums[i] - nums[i - 1])
            if diff > max_diff:
                max_diff = diff
        
        # Finally, check the circular adjacency between last and first
        wrap_diff = abs(nums[-1] - nums[0])
        if wrap_diff > max_diff:
            max_diff = wrap_diff
        
        return max_diff
