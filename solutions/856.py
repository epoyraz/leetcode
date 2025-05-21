class Solution(object):
    def consecutiveNumbersSum(self, n):
        res = 0
        k = 1
        while k * (k + 1) // 2 <= n:
            if (n - k * (k + 1) // 2) % k == 0:
                res += 1
            k += 1
        return res
