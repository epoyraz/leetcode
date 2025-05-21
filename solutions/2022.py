class Solution:
    def maxAlternatingSum(self, nums):
        even, odd = 0, 0
        for num in nums:
            new_even = max(even, odd + num)
            new_odd = max(odd, even - num)
            even, odd = new_even, new_odd
        return even
