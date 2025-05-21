class Solution:
    def sumOfFlooredPairs(self, nums):
        mod = 10**9 + 7
        maxv = max(nums)
        # frequency array
        f = [0] * (maxv + 1)
        for x in nums:
            f[x] += 1
        # prefix sums of frequencies
        pref = [0] * (maxv + 1)
        for i in range(1, maxv + 1):
            pref[i] = pref[i - 1] + f[i]
        ans = 0
        # for each divisor y
        for y in range(1, maxv + 1):
            fy = f[y]
            if fy == 0:
                continue
            Sy = 0
            # sum floor(x / y) * freq(x) over x
            maxk = maxv // y
            for k in range(1, maxk + 1):
                l = k * y
                r = min(maxv, l + y - 1)
                cnt = pref[r] - pref[l - 1]
                Sy += k * cnt
            ans = (ans + fy * Sy) % mod
        return ans
