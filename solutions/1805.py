class Solution(object):
    def minMoves(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Collect the indices of 1's
        pos = [i for i, x in enumerate(nums) if x == 1]
        m = len(pos)
        # b[i] = pos[i] - i; this array is nonâdecreasing
        b = [pos[i] - i for i in range(m)]
        # prefix sums of b
        prefix = [0] * (m + 1)
        for i in range(m):
            prefix[i+1] = prefix[i] + b[i]
        
        # Slide a window of length k over b to compute
        # sum of abs distances to the window's median in O(1) each.
        ans = float('inf')
        for i in range(m - k + 1):
            j = i + k - 1
            mid = i + k // 2
            median = b[mid]
            # # of elements to the left of median in window
            left_count = mid - i
            # # of elements to the right of median
            right_count = j - mid
            # sum of left segment
            left_sum = prefix[mid] - prefix[i]
            # sum of right segment
            right_sum = prefix[j+1] - prefix[mid+1]
            
            # cost = sum(median - b[l]) + sum(b[r] - median)
            cost = median * left_count - left_sum \
                   + right_sum - median * right_count
            ans = min(ans, cost)
        
        # If k == 1, ans stays inf; but no moves needed
        return 0 if k == 1 else ans
