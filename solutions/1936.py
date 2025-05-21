class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        MOD = 10**9 + 7
        k = primeFactors
        if k <= 3:
            return k
        c3, r = divmod(k, 3)
        if r == 0:
            return pow(3, c3, MOD)
        elif r == 1:
            # turn one 3+1 into 2+2
            return (pow(3, c3-1, MOD) * 4) % MOD
        else:  # r == 2
            return (pow(3, c3, MOD) * 2) % MOD
