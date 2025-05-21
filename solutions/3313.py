class Solution(object):
    def maximumStrength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int  # guaranteed odd
        :rtype: int
        """
        import math
        
        # Precompute the weight for choosing segment j:
        # w[j] = (-1)^(j-1) * (k - j + 1), 1-based
        w = [0]*(k+1)
        for j in range(1, k+1):
            sign = -1 if (j-1)%2 else 1
            w[j] = sign * (k - j + 1)
        
        # end[j]: best strength for j segments, with the j-th ending exactly here
        # any_[j]: best strength for j segments ending anywhere so far
        end = [-10**30]*(k+1)
        any_ = [-10**30]*(k+1)
        any_[0] = 0  # zero segments gives strength 0
        
        for x in nums:
            # update in descending j to avoid overwriting what we need
            for j in range(k, 0, -1):
                extend = end[j] + w[j] * x
                start  = any_[j-1] + w[j] * x
                new_end_j = extend if extend > start else start
                end[j] = new_end_j
                # record best so far for j segments
                if new_end_j > any_[j]:
                    any_[j] = new_end_j
        
        return any_[k]
