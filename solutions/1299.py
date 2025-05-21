class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def kadane(nums):
            max_end = max_so_far = 0
            for x in nums:
                max_end = max(x, max_end + x)
                max_so_far = max(max_so_far, max_end)
            return max_so_far

        one = kadane(arr)
        if k == 1:
            return one % MOD

        total_sum = sum(arr)
        two = kadane(arr * 2)

        if total_sum > 0:
            return (two + (k - 2) * total_sum) % MOD
        else:
            return two % MOD
