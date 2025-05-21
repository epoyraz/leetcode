class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # If there's any element below k, we can never bring it up.
        if any(x < k for x in nums):
            return -1
        
        # Count how many distinct values exceed k.
        distinct_vals = set(nums)
        # Each distinct value > k will require exactly one chop.
        return sum(1 for v in distinct_vals if v > k)
