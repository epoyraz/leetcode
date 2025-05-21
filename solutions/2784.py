class Solution:
    def sumOfPower(self, nums):
        MOD = 10**9 + 7
        nums.sort()
        res = 0
        prefix_sum = 0

        for num in nums:
            # For each num as max, calculate power
            res = (res + num * num % MOD * (num + prefix_sum)) % MOD
            prefix_sum = (2 * prefix_sum + num) % MOD

        return res
