class Solution(object):
    def minOperations(self, nums):
        sum_bits = 0
        max_num = 0
        for num in nums:
            sum_bits += bin(num).count('1')
            if num > max_num:
                max_num = num
        doubling = max_num.bit_length() - 1 if max_num > 0 else 0
        return sum_bits + doubling
