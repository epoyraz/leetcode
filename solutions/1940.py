class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        mask = (1 << maximumBit) - 1
        total_xor = 0
        for x in nums:
            total_xor ^= x
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            # at this step, total_xor is XOR of nums[0..n-1-i]
            ans[i] = total_xor ^ mask
            # remove the last element for next step
            total_xor ^= nums[n-1-i]
        return ans
