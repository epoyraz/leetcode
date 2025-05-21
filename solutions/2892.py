class Solution:
    def isGood(self, nums):
        n = max(nums)
        if len(nums) != n + 1:
            return False
        count = [0] * (n + 1)
        for num in nums:
            if num > n:
                return False
            count[num - 1] += 1
        for i in range(n - 1):
            if count[i] != 1:
                return False
        return count[n - 1] == 2
