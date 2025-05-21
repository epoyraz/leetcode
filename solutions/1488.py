class Solution(object):
    def getKth(self, lo, hi, k):
        memo = {}

        def power(x):
            if x == 1:
                return 0
            if x in memo:
                return memo[x]
            if x % 2 == 0:
                memo[x] = 1 + power(x // 2)
            else:
                memo[x] = 1 + power(3 * x + 1)
            return memo[x]

        nums = list(range(lo, hi + 1))
        nums.sort(key=lambda x: (power(x), x))
        return nums[k - 1]
