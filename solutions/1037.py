class Solution:
    def minKBitFlips(self, nums, k):
        n = len(nums)
        flips = 0
        flip = 0
        is_flipped = [0] * n

        for i in range(n):
            if i >= k:
                flip ^= is_flipped[i - k]
            if nums[i] ^ flip == 0:
                if i + k > n:
                    return -1
                flips += 1
                flip ^= 1
                is_flipped[i] = 1

        return flips
