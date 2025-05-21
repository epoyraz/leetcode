import functools

class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If nums empty
        if not nums:
            return 0
        # Determine size for FWHT: next power of two > max possible XOR
        maxv = max(nums)
        size = 1 << (maxv.bit_length())
        # Presence vector
        P = [0] * size
        for v in nums:
            P[v] = 1
        # Fast Walsh-Hadamard Transform for XOR-convolution
        def fwht(a, inverse=False):
            n = len(a)
            h = 1
            while h < n:
                for i in range(0, n, h*2):
                    for j in range(i, i+h):
                        x = a[j]
                        y = a[j+h]
                        a[j] = x + y
                        a[j+h] = x - y
                h *= 2
            if inverse:
                for i in range(n):
                    a[i] //= n
        # Convolve P with itself three times
        A = P[:]
        fwht(A)
        # Pointwise cube for triple convolution
        for i in range(size):
            A[i] = A[i] ** 3
        fwht(A, inverse=True)
        # Count how many XOR values are achievable (A[x] > 0)
        # We only care about XOR results within [0..size)
        count = 0
        for x in range(size):
            if A[x] > 0:
                count += 1
        return count