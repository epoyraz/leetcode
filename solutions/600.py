class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        # fib[i] = number of binary strings of length i without consecutive ones
        fib = [0] * 32
        fib[0] = 1
        fib[1] = 2
        for i in range(2, 32):
            fib[i] = fib[i-1] + fib[i-2]

        ans = 0
        prev_bit = 0
        # process bits from most significant to least
        k = n.bit_length()  # number of bits needed to represent n
        for i in range(k-1, -1, -1):
            if (n >> i) & 1:
                # if this bit is 1, add all valid combinations with a 0 here
                ans += fib[i]
                # if previous bit was also 1, we've formed '11', stop here
                if prev_bit:
                    return ans
                prev_bit = 1
            else:
                prev_bit = 0

        # if we never saw consecutive ones in n itself, include n
        return ans + 1
