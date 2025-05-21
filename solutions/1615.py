class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        MOD = 10**9 + 7
        sub_sums = []

        # Generate all subarray sums
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                sub_sums.append(total)

        sub_sums.sort()

        # Sum from left to right (1-based index)
        return sum(sub_sums[left - 1:right]) % MOD
