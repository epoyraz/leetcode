class Solution(object):
    def nonSpecialCount(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        import math
        
        # integer sqrt helper
        def isqrt(n):
            x = int(n**0.5)
            # adjust for floating-point drift
            while (x+1)*(x+1) <= n:
                x += 1
            while x*x > n:
                x -= 1
            return x
        
        lo = isqrt(l)
        if lo*lo < l:
            lo += 1
        hi = isqrt(r)
        
        if lo > hi:
            # no squares in [l,r]
            return r - l + 1
        
        # sieve primes up to hi
        m = hi + 1
        sieve = [True] * m
        sieve[0] = sieve[1] = False
        for i in xrange(2, int(m**0.5) + 1):
            if sieve[i]:
                step = i
                start = i*i
                for j in xrange(start, m, step):
                    sieve[j] = False
        
        # count primes p in [lo..hi]
        cnt_special = 0
        for p in xrange(lo, hi+1):
            if sieve[p]:
                cnt_special += 1
        
        return (r - l + 1) - cnt_special
