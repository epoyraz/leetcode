class Solution:
    def leastOpsExpressTarget(self, x, target):
        def cost(i):          # operators to write x^i once (without leading + / -)
            return 2 if i == 0 else i

        dp0, dp1 = 0, float('inf')    # dp0: no carry, dp1: carry = 1 to next digit
        i = 0
        t = target

        while t:
            d = t % x                 # current base-x digit
            t //= x
            c = cost(i)

            next0 = min(dp0 + d * c,           # keep carry 0
                         dp1 + (d + 1) * c)    # resolve previous carry-1
            next1 = min(dp0 + (x - d) * c,     # create new carry-1
                         dp1 + (x - d - 1) * c)

            dp0, dp1 = next0, next1
            i += 1

        ans = min(dp0, dp1 + cost(i)) - 1      # minus 1: first term has no leading op
        return ans
