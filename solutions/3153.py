class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        # Count how many times each bit appears across all numbers
        max_num = max(nums)
        B = max_num.bit_length()  # up to ~30
        cnt = [0] * B
        for v in nums:
            for b in range(B):
                if (v >> b) & 1:
                    cnt[b] += 1

        # For i = 1..k, build Xi = OR of bits b where cnt[b] >= i
        ans = 0
        # We'll accumulate ans mod MOD
        for i in range(1, k + 1):
            x = 0
            for b in range(B):
                if cnt[b] >= i:
                    x |= (1 << b)
            ans = (ans + x * x) % MOD

        return ans
