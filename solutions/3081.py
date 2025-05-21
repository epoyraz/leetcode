class Solution(object):
    def minLengthAfterRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Check if we can form k pairs: nums[i] < nums[n-k+i] for all i in [0..k-1]
        def can_pair(k):
            for i in range(k):
                if nums[i] >= nums[n - k + i]:
                    return False
            return True
        
        # Binary search maximum k in [0..n//2]
        lo, hi = 0, n // 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_pair(mid):
                lo = mid
            else:
                hi = mid - 1
        
        # lo = maximum number of pairs we can remove
        return n - 2 * lo
