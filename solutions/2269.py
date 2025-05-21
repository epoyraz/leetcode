class Solution:
    def countElements(self, nums):
        mn = min(nums)
        mx = max(nums)
        return sum(1 for x in nums if mn < x < mx)
