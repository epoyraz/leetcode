class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        total = 0

        for i, val in enumerate(arr):
            # number of ways to choose start j in [0..i]
            L = i + 1
            left_even = (i // 2) + 1
            left_odd = L - left_even

            # number of ways to choose end k in [i..n-1]
            R = n - i
            if i % 2 == 0:
                right_even = (R + 1) // 2
                right_odd = R - right_even
            else:
                right_odd = (R + 1) // 2
                right_even = R - right_odd

            # only pairs (j,k) with same parity give odd-length subarray
            count = left_even * right_even + left_odd * right_odd
            total += val * count

        return total
