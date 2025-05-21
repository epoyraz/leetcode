class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        odd = 0
        even = 1  # empty prefix
        total = 0
        prefix = 0

        for num in arr:
            prefix += num
            if prefix % 2 == 0:
                total += odd
                even += 1
            else:
                total += even
                odd += 1

        return total % MOD
