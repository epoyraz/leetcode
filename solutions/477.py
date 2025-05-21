class Solution:
    def totalHammingDistance(self, nums):
        total = 0
        n = len(nums)
        for i in range(32):  # Since nums[i] <= 10^9, only 32 bits needed
            count_ones = sum((num >> i) & 1 for num in nums)
            total += count_ones * (n - count_ones)
        return total
