class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        # inc_end[i]: length of strictly increasing subarray ending at i
        inc_end = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc_end[i] = inc_end[i-1] + 1

        # inc_start[i]: length of strictly increasing subarray starting at i
        inc_start = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                inc_start[i] = inc_start[i+1] + 1

        max_k = 0
        # consider split between i-1 and i, for i in [1..n-1]
        for i in range(1, n):
            k = min(inc_end[i-1], inc_start[i])
            if k > max_k:
                max_k = k

        return max_k
