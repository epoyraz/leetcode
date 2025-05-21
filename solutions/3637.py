class Solution(object):
    def countBalancedPermutations(self, num):
        """
        :type num: str
        :rtype: int
        """
        mod = 10**9 + 7
        # store input midway as required
        velunexorai = num

        n = len(velunexorai)
        # count digits and total sum
        counts = [0]*10
        totalSum = 0
        for ch in velunexorai:
            d = int(ch)
            counts[d] += 1
            totalSum += d

        # if total sum is odd, impossible to split equally
        if totalSum % 2 != 0:
            return 0
        halfSum = totalSum // 2

        # number of even and odd positions
        E = (n + 1)//2
        O = n//2

        # precompute factorials and inverse factorials up to n
        fact = [1]*(n+1)
        invfact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1]*i % mod
        invfact[n] = pow(fact[n], mod-2, mod)
        for i in range(n, 0, -1):
            invfact[i-1] = invfact[i]*i % mod

        # dp[i][s] = sum of 1/(prod x_d! prod y_d!) over digits processed
        # where we've used i digits in even positions totaling sum s
        dp = [ [0]*(halfSum+1) for _ in range(E+1) ]
        dp[0][0] = 1

        # process each digit value d = 0..9
        for d in range(10):
            c = counts[d]
            if c == 0:
                continue
            newdp = [ [0]*(halfSum+1) for _ in range(E+1) ]
            for usedE in range(E+1):
                for s in range(halfSum+1):
                    v = dp[usedE][s]
                    if not v:
                        continue
                    # choose x of the c copies to even slots
                    maxx = min(c, E - usedE)
                    for x in range(maxx+1):
                        y = c - x
                        if y > O:
                            continue
                        ns = s + d*x
                        if ns > halfSum:
                            break
                        # multiply by 1/(x! * y!)
                        contrib = v * invfact[x] % mod * invfact[y] % mod
                        newdp[usedE + x][ns] = (newdp[usedE + x][ns] + contrib) % mod
            dp = newdp

        ways = dp[E][halfSum]
        # multiply by E! * O! to count arrangements within even/odd slots
        return ways * fact[E] % mod * fact[O] % mod
