class Solution:
    def numberOfGoodSubarraySplits(self, nums):
        MOD = 10**9 + 7
        ones = [i for i, num in enumerate(nums) if num == 1]

        if not ones:
            return 0

        ans = 1
        for i in range(1, len(ones)):
            gap = ones[i] - ones[i - 1] - 1
            ans = (ans * (gap + 1)) % MOD

        return ans
