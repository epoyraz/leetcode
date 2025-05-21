class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from functools import reduce
        import operator

        # XOR of all elements in the array
        xor_total = reduce(operator.xor, nums)

        # XOR difference between desired value and current total
        xor_needed = xor_total ^ k

        # Count the number of 1s in xor_needed â each 1 corresponds to a bit flip needed
        return bin(xor_needed).count('1')
