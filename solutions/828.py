class Solution(object):
    def xorGame(self, nums):
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        return xor_sum == 0 or len(nums) % 2 == 0
