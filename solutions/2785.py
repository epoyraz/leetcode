class Solution:
    def semiOrderedPermutation(self, nums):
        n = len(nums)
        i = nums.index(1)
        j = nums.index(n)
        if i < j:
            return i + (n - 1 - j)
        else:
            return i + (n - 1 - j) - 1
