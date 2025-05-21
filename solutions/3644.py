class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        # build prefix sums
        P = [0] * (n+1)
        for i in range(1, n+1):
            P[i] = P[i-1] + nums[i-1]
        
        best = float('inf')
        # try all subarrays of length between l and r
        for end in range(1, n+1):
            # subarray length â from l..r
            for length in range(l, r+1):
                start = end - length
                if start < 0:
                    continue
                s = P[end] - P[start]
                if 0 < s < best:
                    best = s
        
        return best if best != float('inf') else -1
