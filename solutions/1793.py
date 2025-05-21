class Solution(object):
    def minMoves(self, nums, limit):
        n = len(nums)
        change = [0] * (2 * limit + 2)
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            lo = min(a, b) + 1
            hi = max(a, b) + limit
            s = a + b
            change[2] += 2
            change[lo] -= 1
            change[s] -= 1
            change[s + 1] += 1
            change[hi + 1] += 1
            change[2 * limit + 1] -= 2
        res = float('inf')
        cur = 0
        for x in range(2, 2 * limit + 1):
            cur += change[x]
            if cur < res:
                res = cur
        return res
