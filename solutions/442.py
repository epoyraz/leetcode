class Solution:
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                res.append(abs(num))
            else:
                nums[idx] *= -1
        return res
