class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        k = n - 1
        # Determine how many bits we need from k
        # i.e. the highest j with (k >> j) > 0
        if k == 0:
            return x
        import math
        max_j = k.bit_length()  # we need j = 0..max_j-1

        # collect free bit positions (where x has a 0 bit)
        free = []
        i = 0
        while len(free) < max_j:
            if ((x >> i) & 1) == 0:
                free.append(i)
            i += 1

        # build t_k by spreading bits of k into those free positions
        t = 0
        for j in range(max_j):
            if (k >> j) & 1:
                t |= (1 << free[j])

        return x + t
