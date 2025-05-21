class Solution(object):
    def countNicePairs(self, nums):
        MOD = 10**9 + 7

        def rev(x):
            y = 0
            while x:
                y = y * 10 + x % 10
                x //= 10
            return y

        count = {}
        ans = 0
        for x in nums:
            diff = x - rev(x)
            c = count.get(diff, 0)
            ans = (ans + c) % MOD
            count[diff] = c + 1
        return ans
